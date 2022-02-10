# Generated by Django 3.2.7 on 2022-02-10 18:46

import confetti.apps.storage.models.member
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberResume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last update time')),
                ('pdf', models.FileField(blank=True, max_length=300, null=True, upload_to=confetti.apps.storage.models.member.generate_cv_upload_path)),
                ('version', models.CharField(blank=True, max_length=300, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_resume', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'member résumé',
                'verbose_name_plural': 'member résumés',
            },
        ),
    ]
