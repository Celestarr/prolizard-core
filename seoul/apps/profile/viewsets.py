from django.db import transaction
from django.db.models.query import QuerySet
from django.utils import timezone

from seoul.apps.common.viewsets import ModelViewSet


class ProfileSectionViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    @property
    def _extra_create_kwargs(self):
        return {"user": self.request.user.pk}

    def get_queryset(self):
        assert self.queryset is not None, (
            f"'{self.__class__.__name__}' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
        )

        queryset = self.queryset

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()

        queryset = queryset.filter(user=self.request.user)

        return queryset

    @staticmethod
    def update_user_profile_version(user):
        user.updated_at = timezone.now()
        user.save()

    def handle_modification_action(self, action, request, *args, **kwargs):
        with transaction.atomic():
            res = getattr(super(), action)(request, *args, **kwargs)
            self.update_user_profile_version(request.user)
            return res

    def create(self, request, *args, **kwargs):
        return self.handle_modification_action("create", request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.handle_modification_action("update", request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return self.handle_modification_action("partial_update", request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.handle_modification_action("destroy", request, *args, **kwargs)
