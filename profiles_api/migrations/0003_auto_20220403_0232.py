# Generated by Django 2.2 on 2022-04-03 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_profiles',
            new_name='user_profile',
        ),
    ]
