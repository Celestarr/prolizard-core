from typing import Dict
from urllib.parse import urljoin

import requests
from django.conf import settings

from confetti.apps.core.models import User
from confetti.apps.member.serializers import MemberProfileSerializerForResumeTemplate


class Passage:
    def __init__(self):
        self.base_url = settings.PASSAGE_SERVER_URL.rstrip("/")

    def process_pdf_template(self, payload):
        url = urljoin(self.base_url, "process-pdf-template")
        res = requests.post(url, json=payload)
        return res.json()

    def make_member_resume(self, member: User, current_version: str) -> Dict[str, str]:
        resume_template = member.member_preference.resume_template
        template_file_name = resume_template.template_file_name
        template_file = settings.DATA_DIR / "pug" / "templates" / "resume" / template_file_name
        path_prefix = ""

        if settings.DEBUG:
            path_prefix = "test/"

        payload = {
            "context": MemberProfileSerializerForResumeTemplate(member).data,
            "template": template_file.read_text(),
            "templateType": "pug",
            "config": resume_template.puppeteer_config,
            "s3": {
                "region": settings.AWS_S3_REGION_NAME,
                "bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "fileName": "{}members/{}/{}.pdf".format(path_prefix, member.id, current_version),
                "accessKeyId": settings.AWS_S3_ACCESS_KEY_ID,
                "secretAccessKey": settings.AWS_S3_SECRET_ACCESS_KEY,
            },
        }

        return self.process_pdf_template(payload)


passage = Passage()

__all__ = ["passage"]
