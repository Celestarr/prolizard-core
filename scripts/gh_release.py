import os
from pathlib import Path
from urllib.parse import urljoin

import requests

REPOSITORY_ROOT = Path(__file__).parent.parent
GITHUB_ACCESS_TOKEN = os.getenv("GH_ACCESS_TOKEN")
GITHUB_API_URL = os.getenv("GITHUB_API_URL")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
PROJECT_NAME = GITHUB_REPOSITORY.split("/")[-1]
PROJECT_VERSION = (REPOSITORY_ROOT / "version.txt").read_text().strip()
DEFAULT_HEADERS = {
    "Authorization": f"token {GITHUB_ACCESS_TOKEN}",
}


def release_exists():
    api_path = f"/repos/{GITHUB_REPOSITORY}/releases/tags/v{PROJECT_VERSION}"
    url = urljoin(GITHUB_API_URL, api_path)
    res = requests.get(url, headers=DEFAULT_HEADERS)

    if not res.ok:
        return False

    return True


def release():
    if not release_exists():
        body = {
            "tag_name": f"v{PROJECT_VERSION}",
            "target_commitish": "master",
            "name": f"{PROJECT_NAME} {PROJECT_VERSION}",
            "draft": False,
            "body": "O_O",
            "prerelease": "pre" in PROJECT_VERSION,
        }

        api_path = f"/repos/{GITHUB_REPOSITORY}/releases"
        url = urljoin(GITHUB_API_URL, api_path)

        requests.post(url, json=body, headers=DEFAULT_HEADERS)


if __name__ == "__main__":
    release()
