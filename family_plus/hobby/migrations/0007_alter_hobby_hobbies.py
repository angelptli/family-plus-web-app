# Generated by Django 3.2.8 on 2021-11-13 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0006_alter_hobby_hobbies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobbies',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
