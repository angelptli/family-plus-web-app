# Generated by Django 3.2.8 on 2021-11-07 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0006_alter_familymember_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website_users.familyprofile'),
        ),
    ]
