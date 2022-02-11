import subprocess

from confetti.apps.core.models.user import User


class LatexCompiler:
    root_command = "pdflatex"
    default_args = ["-halt-on-error", "-file-line-error", "-interaction=nonstopmode"]

    def exec(self, file_name: str, cwd=None):
        result = subprocess.run(
            [self.root_command] + self.default_args + [file_name],
            cwd=cwd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        if result.returncode != 0:
            return False

        return True


latex_compiler = LatexCompiler()

__all__ = ["latex_compiler"]
