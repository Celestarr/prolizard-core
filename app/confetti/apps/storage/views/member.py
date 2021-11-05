from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.shortcuts import redirect
from django.views.generic import ListView

from confetti.apps.core.models import User
from confetti.apps.storage.models import MemberResume
from confetti.services import passage
from confetti.utils import hash_string


class DownloadResumeView(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):
        del request, args

        member_username = kwargs["member_username"]

        try:
            member = User.objects.get(username=member_username)
        except User.DoesNotExist:
            raise Http404()

        try:
            resume = MemberResume.objects.get(member=member)
        except MemberResume.DoesNotExist:
            resume = MemberResume.objects.create(member=member)

        current_version = hash_string(str(member.updated_at))

        if not resume.download_url or resume.version != current_version:
            res = passage.make_member_resume(member, current_version)
            resume.download_url = res["downloadUrl"]
            resume.version = current_version
            resume.save()

        return redirect(resume.download_url)


__all__ = ["DownloadResumeView"]
