# Generated by Django 4.0.2 on 2022-02-20 08:08

import apps.identity.validators
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last update time')),
                ('about', models.CharField(blank=True, max_length=1000, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, error_messages={'blank': 'Enter a valid email address.', 'invalid': 'Enter a valid email address.', 'unique': 'Email is invalid or already taken.'}, max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='first name')),
                ('headline', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('last_name', models.CharField(blank=True, max_length=50, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='last name')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='password')),
                ('username', models.CharField(blank=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 3 to 30 characters. Letters (a-z), digits (0-9) and underscore (_) only.', max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(1), apps.identity.validators.UsernameValidator()], verbose_name='username')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', to='common.country')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_set', to='common.gender')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
