# Generated by Django 3.2.8 on 2021-11-07 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('age_range', '0002_agerange_family_member_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AgeRange',
        ),
    ]
