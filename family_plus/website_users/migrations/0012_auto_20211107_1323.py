# Generated by Django 3.2.8 on 2021-11-07 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_users', '0011_alter_familymember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website_users.familyprofile'),
        ),
        migrations.AlterField(
            model_name='familyprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
