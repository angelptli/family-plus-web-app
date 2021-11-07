# Generated by Django 3.2.8 on 2021-11-07 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('website_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Weekdays', 'Weekdays'), ('Weekends', 'Weekends')], max_length=255, null=True)),
                ('time_of_day', models.CharField(choices=[('Morning', 'Morning'), ('Noon', 'Noon'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening'), ('Night', 'Night'), ('Anytime', 'Anytime'), ('Unknown', 'Unknown')], max_length=255, null=True)),
                ('family_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='website_users.familyprofile')),
            ],
        ),
    ]
