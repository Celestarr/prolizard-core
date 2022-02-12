import shutil
from pathlib import Path
from typing import Optional

from django.conf import settings
from django.template.loader import render_to_string

from apps.core.models.user import User

from .latex import latex_compiler


def generate_cv_pdf(user: User, version: str) -> Optional[Path]:
    """
    1. template to file in particular directory
    2. compile with latex_compiler
    3. upload file
    """
    del version

    template = user.member_preference.resume_template
    ctx = {"user": user}
    content = render_to_string(f"latex/{template.slug}/{template.template_entrypoint}", context=ctx)
    target_dir = settings.CV_TEMPLATE_TEMPORARY_DIR / f"{str(user.id)}_{template.slug}"

    # Clear directory (if exists)
    shutil.rmtree(str(target_dir.absolute()), ignore_errors=True)

    # Re-create directory
    target_dir.mkdir(parents=True, exist_ok=True)

    with open(str((target_dir / "main.tex").absolute()), "w+", encoding="utf-8") as file:
        file.write(content)

    succeeded = latex_compiler.exec("main.tex", cwd=str(target_dir.absolute()))

    if succeeded:
        return target_dir / "main.pdf"

    return None
