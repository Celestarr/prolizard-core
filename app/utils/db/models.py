from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.utils.string import snake_to_capitalized


class BaseModel(models.Model):
    """
    Base model

    Attributes:
        user_editable_fields: Fields that can be edited by the user.
    """

    user_editable_fields = []

    @staticmethod
    def get_field_type(field):
        if isinstance(field, models.CharField):
            return "string"
        elif isinstance(field, models.DateField):
            return "date"
        elif isinstance(field, models.DateTimeField):
            return "datetime"
        elif isinstance(field, models.EmailField):
            return "email"
        elif isinstance(field, models.IntegerField):
            return "integer"
        # Add more field types as needed
        else:
            return "unknown"

    def get_form_field_config(self):
        field_configs = []

        for field in self._meta.fields:
            if field.name not in self.user_editable_fields:
                continue

            field_config = {
                "name": field.name,
                "type": self.get_field_type(field),
                "required": not field.null,
                "verbose_name": snake_to_capitalized(field.name),
            }

            if field.choices:
                field_config["choices"] = field.choices

            if field.help_text:
                field_config["help_text"] = field.help_text

            # if field.verbose_name:
            #     field_config["verbose_name"] = field.verbose_name

            if hasattr(field, "max_length") and field.max_length:
                field_config["max_length"] = field.max_length

            if hasattr(field, "min_length") and field.validators:
                min_length_validators = [v.limit_value for v in field.validators if isinstance(v, MinLengthValidator)]

                if min_length_validators:
                    field_config["min_length"] = min_length_validators[0]

            field_configs.append(field_config)

        return field_configs

    def get_form_layout_config(self):
        # 'layout': [
        #     {'row': 1, 'fields': ['username'], 'sizes': [100]},
        #     {'row': 2, 'fields': ['email', 'first_name'], 'sizes': [50, 50]},
        #     {'row': 3, 'fields': ['last_name'], 'sizes': [100]},
        # ]
        raise NotImplementedError

    class Meta:
        abstract = True


class TimeStampedModel(BaseModel):
    created_at = models.DateTimeField(_("creation time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("last update time"), auto_now=True)

    objects = models.Manager()

    class Meta:
        abstract = True


class TimeStampedModelWithSmallId(TimeStampedModel):
    id = models.SmallAutoField(primary_key=True)

    class Meta:
        abstract = True
