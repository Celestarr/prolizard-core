from django.core.files import File
from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.core.models import User
from apps.core.viewsets import ModelViewSet
from apps.storage.models import MemberResume
from services.cv import generate_cv_pdf
from utils import hash_string
from utils.django import build_file_field_download_url, remove_media_file


class DownloadResumeViewSet(ModelViewSet):
    permission_classes_by_action = {}
    permission_classes = (IsAuthenticated,)
    http_method_names = ["get", "head", "options"]
    queryset = User.objects.all()
    lookup_field = "username"

    @staticmethod
    def should_update(resume: MemberResume, current_version: str) -> bool:
        return not resume.pdf or resume.version != current_version

    def retrieve(self, request, *args, **kwargs):
        del args, kwargs

        member = self.get_object()

        try:
            resume = MemberResume.objects.get(member=member)
        except MemberResume.DoesNotExist:
            resume = MemberResume.objects.create(member=member)

        current_version = hash_string(str(member.updated_at))

        if self.should_update(resume, current_version):
            with transaction.atomic():
                # Acquire db-level lock to make sure only one of many request is
                # updating download url and version.
                resume = MemberResume.objects.select_for_update().get(member=member)

                # Check pre-condition again because it's possible for columns
                # to be changed by others during lock-acquiring period.
                if self.should_update(resume, current_version):
                    pdf_path = generate_cv_pdf(member, current_version)

                    if not pdf_path:
                        raise Exception("Could not generate pdf.")

                    target_file_name = f"user_{member.id}.pdf"

                    remove_media_file(f"cv/{target_file_name}")

                    with open(str(pdf_path.absolute()), "rb") as file:
                        resume.pdf = File(file, name=target_file_name)
                        resume.version = current_version
                        resume.save()
                else:
                    # Reload the object in the event of an update during
                    # lock acquiring period.
                    resume = MemberResume.objects.get(member=member)

        return Response(
            {
                "download_url": build_file_field_download_url(request, resume.pdf),
            }
        )


__all__ = ["DownloadResumeViewSet"]
