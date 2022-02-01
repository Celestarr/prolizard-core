import os
from pathlib import Path

import requests

version_file = Path(__file__).parent.parent / "version.txt"
version = version_file.read_text().strip()
headers = {
    "Authorization": "token {}".format(os.getenv("GH_ACCESS_TOKEN")),
}


def release_exists():
    res = requests.get(
        "https://api.github.com/repos/myfolab/confetti/releases/tags/v{}".format(version), headers=headers
    )

    if not res.ok:
        return False

    return True


def release():
    if not release_exists():
        body = {
            "tag_name": "v{}".format(version),
            "target_commitish": "master",
            "name": "confetti {}".format(version),
            "draft": False,
            "body": "O_O",
            "prerelease": "pre" in version,
        }

        requests.post("https://api.github.com/repos/myfolab/confetti/releases", json=body, headers=headers)


if __name__ == "__main__":
    release()
