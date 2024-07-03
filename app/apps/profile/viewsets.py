from django.db import transaction
from django.db.models.query import QuerySet
from django.utils import timezone

from app.apps.common.viewsets import UserModelViewSet


class ProfileSectionViewSet(UserModelViewSet):  # pylint: disable=too-many-ancestors
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
