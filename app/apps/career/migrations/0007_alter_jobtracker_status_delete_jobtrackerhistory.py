# Generated by Django 5.0.6 on 2024-07-10 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_rename_company_name_jobtracker_organization_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtracker',
            name='status',
            field=models.CharField(blank=True, choices=[('accepted_offer', 'Accepted Offer'), ('applied', 'Applied'), ('draft', 'Draft'), ('offer_stage', 'Offer Stage'), ('interviewing', 'Interviewing'), ('no_response', 'No Response'), ('rejected_applicant', 'Rejected (Applicant Withdrew)'), ('rejected_organization', 'Rejected (Organization Decision)')], max_length=50),
        ),
        migrations.DeleteModel(
            name='JobTrackerHistory',
        ),
    ]
