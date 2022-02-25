import shutil

from django.conf import settings
from django.template.loader import render_to_string

from apps.identity.models import User

from .latex import latex_compiler


class ResumePDFGenerator:
    def __init__(self, user: User, version: str):
        self.pdf_path = None
        self.user = user
        self.version = version
        template = user.preference.resume_template
        self.template = template
        self.target_dir = settings.RESUME_TEMPLATE_TEMPORARY_DIR / f"{str(user.id)}_{template.slug}"

    def remove_target_directory(self, silent=False):
        shutil.rmtree(str(self.target_dir.absolute()), ignore_errors=silent)

    def __enter__(self):
        user = self.user
        target_dir = self.target_dir
        template = self.template
        ctx = {"user": user}
        content = render_to_string(f"latex/{template.slug}/{template.template_entrypoint}", context=ctx)

        # Clear directory (if exists)
        self.remove_target_directory(silent=True)

        # Re-create directory
        target_dir.mkdir(parents=True, exist_ok=True)

        with open(str((target_dir / "main.tex").absolute()), "w+", encoding="utf-8") as file:
            file.write(content)

        succeeded = latex_compiler.exec("main.tex", cwd=str(target_dir.absolute()))

        if succeeded:
            self.pdf_path = target_dir / "main.pdf"
            return self

        raise RuntimeError("Error occurred in latex compiler.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # failed = exc_val is not None
        self.remove_target_directory()
