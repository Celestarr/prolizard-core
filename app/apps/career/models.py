from django.db import models

from app.utils.db.models import TimeStampedModel


class JobTracker(TimeStampedModel):
    """
    Model to track personal job applications.
    """

    # Use DateField for application date and deadline (if applicable)
    application_date = models.DateField(blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)

    country = models.ForeignKey(
        "core.Country",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="job_tracker_set",
    )

    # Add an optional field for interview round details
    interview_round = models.CharField(blank=True, max_length=50, null=True)

    # Add an optional field for any notes
    notes = models.TextField(blank=True, null=True)

    organization_name = models.CharField(blank=True, max_length=255)

    position_title = models.CharField(blank=True, max_length=255)

    # Use choices for a controlled vocabulary of application statuses
    STATUS_CHOICES = (
        ("accepted_offer", "Accepted Offer"),
        ("applied", "Applied"),
        ("draft", "Draft"),
        ("offer_stage", "Offer Stage"),
        ("interviewing", "Interviewing"),
        ("no_response", "No Response"),
        ("rejected_applicant", "Rejected (Applicant Withdrew)"),
        ("rejected_organization", "Rejected (Organization Decision)"),
    )
    status = models.CharField(blank=True, max_length=50, choices=STATUS_CHOICES)

    user = models.ForeignKey("user_management.User", on_delete=models.CASCADE, related_name="job_tracker_set")

    user_editable_fields = [
        "application_date",
        "application_deadline",
        "interview_round",
        "notes",
        "organization_name",
        "position_title",
        "status",
    ]

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.organization_name} - {self.position_title} ({self.status})"

    def get_form_layout_config(self):
        return [
            {"row": 1, "fields": ["position_title"], "sizes": [12]},
            {"row": 2, "fields": ["organization_name"], "sizes": [12]},
            {"row": 3, "fields": ["application_date", "application_deadline"], "sizes": [6, 6]},
            {"row": 4, "fields": ["interview_round", "status"], "sizes": [6, 6]},
            {"row": 5, "fields": ["notes"], "sizes": [12]},
        ]
