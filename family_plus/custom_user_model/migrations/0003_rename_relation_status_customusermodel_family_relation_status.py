# Generated by Django 3.2.8 on 2021-10-29 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user_model', '0002_auto_20211028_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customusermodel',
            old_name='relation_status',
            new_name='family_relation_status',
        ),
    ]