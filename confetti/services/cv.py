from django.template.loader import render_to_string

from confetti.apps.core.models.user import User
from django.conf import settings
from tempfile import NamedTemporaryFile
from .latex import latex_compiler


def generate_cv_pdf(user: User, version: str):
    """
    1. template to file in particular directory
    2. compile with latex_compiler
    3. upload file
    """

    template = user.member_preference.resume_template
    ctx = {
        'user': user
    }
    content = render_to_string(f'latex/{template.slug}/{template.template_entrypoint}', context=ctx)
    target_dir = settings.CV_TEMPLATE_TEMPORARY_DIR / f'{str(user.id)}_{template.slug}_{version}'
    target_dir.mkdir(parent=True, exist_ok=True)

    with open(str((target_dir / 'main.tex').absolute()), 'w+') as f:
        f.write(content)

    latex_compiler.exec('main.tex', cwd=str(target_dir.absolute()))
