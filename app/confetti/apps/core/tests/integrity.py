from datetime import datetime, timezone

from django.test import TestCase

from confetti.apps.core.models.confirmation_key import ConfirmationKey


class DBIntegrityTestCase(TestCase):
    def test_fail_duplicate_confirmation_key(self):
        ConfirmationKey.objects.create(key="key", expires_at=datetime.now(tz=timezone.utc))
        ConfirmationKey.objects.create(key="key", expires_at=datetime.now(tz=timezone.utc))
