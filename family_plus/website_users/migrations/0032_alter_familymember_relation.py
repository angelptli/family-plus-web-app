# Generated by Django 3.2.8 on 2021-11-13 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0031_alter_familymember_age_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='relation',
            field=models.CharField(blank=True, choices=[('Mother', 'Mother'), ('Father', 'Father'), ('Daughter', 'Daughter'), ('Son', 'Son'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('Cousin', 'Cousin'), ('Parent', 'Parent'), ('Guardian', 'Guardian'), ('Foster Mother', 'Foster Mother'), ('Foster Father', 'Foster Father'), ('Foster Parent', 'Foster Parent'), ('Grandmother', 'Grandmother'), ('Grandfather', 'Grandfather'), ('Grandparent', 'Grandparent'), ('Relative', 'Relative'), ('Relative-In-Law', 'Relative-In-Law'), ('Family Friend', 'Family Friend'), ('Pet', 'Pet'), ('Other', 'Other')], max_length=50, null=True),
        ),
    ]
