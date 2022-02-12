"""
Django settings for this project.
"""
# pylint: disable=wrong-import-position
# flake8: noqa

from dotenv import load_dotenv

load_dotenv()

from .apps import *
from .auth import *
from .common import *
from .core import *
from .database import *
from .i18n import *
from .middleware import *
from .rest_framework import *
from .static import *
