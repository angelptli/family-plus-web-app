# Generated by Django 3.2.8 on 2021-11-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website_users', '0028_alter_familymember_age_range'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='age_range',
            field=models.CharField(blank=True, choices=[('Child', 'Child'), ('On the way', 'On the way'), ('Baby (0-12 months old)', 'Baby (0-12 months old)'), ('Toddler (1-3 years old)', 'Toddler (1-3 years old)'), ('Preschooler (3-5 years old)', 'Preschooler (3-5 years old)'), ('Gradeschooler (5-12 years old)', 'Gradeschooler (5-12 years old)'), ('Teenager (12-17 years old)', 'Teenager (12-17 years old)'), ('Adult', 'Adult'), ('Adult (18-24 years old)', 'Adult (18-24 years old)'), ('Adult (25-29 years old)', 'Adult (25-29 years old)'), ('Adult (30-34 years old)', 'Adult (30-34 years old)'), ('Adult (35-39 years old)', 'Adult (35-39 years old)'), ('Adult (40-44 years old)', 'Adult (40-45 years old)'), ('Adult (45-49 years old)', 'Adult (45-49 years old)'), ('Adult (50-54 years old)', 'Adult (50-54 years old)'), ('Adult (55-59 years old)', 'Adult (55-59 years old)'), ('Adult (60-64 years old)', 'Adult (60-64 years old)'), ('Older Adult', 'Older Adult'), ('Older Adult (65-69 years old)', 'Older Adult (65-69 years old)'), ('Older Adult (70-74 years old)', 'Older Adult (70-74 years old)'), ('Older Adult (75-79 years old)', 'Older Adult (75-79 years old)'), ('Older Adult (80-84 years old)', 'Older Adult (80-84 years old)'), ('Older Adult (85-89 years old)', 'Older Adult (85-89 years old)'), ('Older Adult (90-94 years old)', 'Older Adult (90-94 years old)'), ('Older Adult (95-99 years old)', 'Older Adult (95-99 years old)'), ('Older Adult (100+ years old)', 'Older Adult (100+ years old)'), ('Senior', 'Senior'), ('Choose not to share', 'Choose not to share')], max_length=100, null=True),
        ),
    ]
