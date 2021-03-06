# Generated by Django 3.2.8 on 2021-11-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0021_alter_familymember_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='relation',
            field=models.CharField(blank=True, choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Daughter', 'Daughter'), ('Son', 'Son'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('Cousin', 'Cousin'), ('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Foster Mother', 'Foster Mother'), ('Foster Father', 'Foster Father'), ('Foster Parent', 'Foster Parent'), ('Grandmother', 'Grandmother'), ('Grandfather', 'Grandfather'), ('Grandparent', 'Grandparent'), ('Relative', 'Relative'), ('Relative-In-Law', 'Relative-In-Law'), ('Family Friend', 'Family Friend'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]
