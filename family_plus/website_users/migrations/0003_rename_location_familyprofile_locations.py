# Generated by Django 3.2.8 on 2021-11-07 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0002_familymember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familyprofile',
            old_name='location',
            new_name='locations',
        ),
    ]
