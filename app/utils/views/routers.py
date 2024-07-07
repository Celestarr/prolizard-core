import re

from rest_framework.routers import SimpleRouter


class HyphenatedSimpleRouter(SimpleRouter):
    def get_urls(self):
        urls = super().get_urls()
        return [self.replace_underscores(url) for url in urls]

    def replace_underscores(self, url):
        if hasattr(url, "pattern"):
            url.pattern.regex = self.replace_underscores_in_pattern(url.pattern.regex)

        return url

    @staticmethod
    def replace_underscores_in_pattern(regex: re.Pattern) -> re.Pattern:
        return re.compile(regex.pattern.replace("_", "-"))
