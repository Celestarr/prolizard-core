# pylint: disable=C0103

from datetime import datetime, timezone

from django.test import TestCase

from apps.core.models.confirmation_key import ConfirmationKey


class DBIntegrityTestCase(TestCase):
    def test_fail_duplicate_confirmation_key(self):
        ConfirmationKey.objects.create(key="key", expires_at=datetime.now(tz=timezone.utc))
        ConfirmationKey.objects.create(key="key", expires_at=datetime.now(tz=timezone.utc))
