from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from confetti.apps.core.models import User
from confetti.apps.core.viewsets import ModelViewSet
from confetti.apps.storage.models import MemberResume
from confetti.utils import aws_s3_create_presigned_url, hash_string
from confetti.services.cv import generate_cv_pdf


class DownloadResumeViewSet(ModelViewSet):
    permission_classes_by_action = {}
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "head", "options"]
    queryset = User.objects.all()
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        del request, args, kwargs

        member = self.get_object()

        try:
            resume = MemberResume.objects.get(member=member)
        except MemberResume.DoesNotExist:
            resume = MemberResume.objects.create(member=member)

        current_version = hash_string(str(member.updated_at))

        if not resume.pdf or resume.version != current_version:
            with transaction.atomic():
                # Acquire db-level lock to make sure only one of many request is
                # updating download url and version.
                resume = MemberResume.objects.select_for_update().get(member=member)

                # Check pre-condition again because it's possible for columns
                # to be changed by others during lock-acquiring period.
                if not resume.pdf or resume.version != current_version:
                    # TODO: Redo, without passage
                    # res = passage.make_member_resume(member, current_version)
                    # resume.download_url = res["downloadUrl"]
                    generate_cv_pdf(member, current_version)
                    resume.version = current_version
                    resume.save()
                else:
                    # Reload the object in the event of an update during
                    # lock acquiring period.
                    resume = MemberResume.objects.get(member=member)

        return Response(
            {
                "download_url": aws_s3_create_presigned_url(resume.download_url, expiration=600),
            }
        )


__all__ = ["DownloadResumeViewSet"]
