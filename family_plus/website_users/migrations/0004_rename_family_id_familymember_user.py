# Generated by Django 3.2.8 on 2021-11-07 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0003_rename_location_familyprofile_locations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familymember',
            old_name='family_id',
            new_name='user',
        ),
    ]
