from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    def get_field_config(self):
        field_configs = []

        for field in self._meta.fields:
            field_config = {
                "name": field.name,
                "type": self.get_field_type(field),
                "required": not field.blank,
            }

            if hasattr(field, "max_length") and field.max_length:
                field_config["max_length"] = field.max_length

            if hasattr(field, "min_length") and field.validators:
                min_length_validators = [v.limit_value for v in field.validators if isinstance(v, MinLengthValidator)]

                if min_length_validators:
                    field_config["min_length"] = min_length_validators[0]

            field_configs.append(field_config)

        return field_configs

    @staticmethod
    def get_field_type(field):
        if isinstance(field, models.CharField):
            return "string"
        elif isinstance(field, models.EmailField):
            return "email"
        elif isinstance(field, models.IntegerField):
            return "integer"
        # Add more field types as needed
        else:
            return "unknown"

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
