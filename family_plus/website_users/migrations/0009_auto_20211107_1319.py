# Generated by Django 3.2.8 on 2021-11-07 21:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website_users', '0008_alter_familymember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyprofile',
            name='connections',
            field=models.ManyToManyField(blank=True, null=True, related_name='connections', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='familyprofile',
            name='hidden',
            field=models.ManyToManyField(blank=True, null=True, related_name='toggled_profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='familyprofile',
            name='pending_requests',
            field=models.ManyToManyField(blank=True, null=True, related_name='requests_pending', to=settings.AUTH_USER_MODEL),
        ),
    ]
