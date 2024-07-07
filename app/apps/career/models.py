from django.db import models

from app.utils.db.models import TimeStampedModel


class JobTracker(TimeStampedModel):
    """
    Model to track personal job applications.
    """

    # Use DateField for application date and deadline (if applicable)
    application_date = models.DateField(blank=True, null=True)
    application_deadline = models.DateField(blank=True, null=True)

    company_name = models.CharField(blank=True, max_length=255)

    # Add an optional field for interview round details
    interview_round = models.CharField(blank=True, max_length=50, null=True)

    # Add an optional field for any notes
    notes = models.TextField(blank=True, null=True)

    position_title = models.CharField(blank=True, max_length=255)

    # Use choices for a controlled vocabulary of application statuses
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("applied", "Applied"),
        ("no_response", "No Response"),
        ("interviewing", "Interviewing"),
        ("offer_stage", "Offer Stage"),
        ("rejected_applicant", "Rejected (Applicant Withdrew)"),
        ("rejected_company", "Rejected (Company Decision)"),
    )
    status = models.CharField(blank=True, max_length=20, choices=STATUS_CHOICES)

    user = models.OneToOneField("identity.User", on_delete=models.CASCADE, related_name="job_tracker")

    def __str__(self):
        return f"{self.company_name} - {self.position_title} ({self.status})"


class JobTrackerHistory(TimeStampedModel):
    """
    Model to track historical changes in JobTracker model.
    """

    current_status = models.CharField(choices=JobTracker.STATUS_CHOICES, max_length=20)
    job_tracker = models.ForeignKey(JobTracker, on_delete=models.CASCADE)
    previous_status = models.CharField(choices=JobTracker.STATUS_CHOICES, max_length=20)

    def __str__(self):
        return f"Job '{self.job_tracker.position_title}' status changed from {self.previous_status} to {self.current_status} on {self.created_at}"
