# Generated by Django 5.0.6 on 2024-07-10 01:31

from django.db import migrations


def rename_status_choices(apps, schema_editor):
    model = apps.get_model('career', 'JobTracker')
    model.objects.filter(status='rejected_company').update(status='rejected_organization')


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0007_alter_jobtracker_status_delete_jobtrackerhistory'),
    ]

    operations = [
        migrations.RunPython(rename_status_choices),
    ]
