from django.db import models
from website_users.models import FamilyMember


class AgeRange(models.Model):
    AGE_RANGE = (
        ('On the way', 'On the way'),
        ('Baby (0-12 months)', 'Baby (0-12 months)'),
        ('Toddler (1-3 years)', 'Toddler (1-3 years)'),
        ('Preschooler (3-5 years)', 'Preschooler (3-5 years)'),
        ('Gradeschooler (5-12 years)', 'Gradeschooler (5-12 years)'),
        ('Teenager (12-17 years)', 'Teenager (12-17 years)'),
        ('Adult (18-24)', 'Adult (18-24)'),
        ('Adult (25-29)', 'Adult (25-29)'),
        ('Adult (30-34)', 'Adult (30-34)'),
        ('Adult (35-39)', 'Adult (35-39)'),
        ('Adult (40-44)', 'Adult (40-45)'),
        ('Adult (45-49)', 'Adult (45-49)'),
        ('Adult (50-54)', 'Adult (50-54)'),
        ('Adult (55-59)', 'Adult (55-59)'),
        ('Adult (60-64)', 'Adult (60-64)'),
        ('Older Adult (65-69)', 'Older Adult (65-69)'),
        ('Older Adult (70-74)', 'Older Adult (70-74)'),
        ('Older Adult (75-79)', 'Older Adult (75-79)'),
        ('Older Adult (80-84)', 'Older Adult (80-84)'),
        ('Older Adult (85-89)', 'Older Adult (85-89)'),
        ('Older Adult (90-94)', 'Older Adult (90-94)'),
        ('Older Adult (95-99)', 'Older Adult (95-99)'),
        ('Older Adult (100+)', 'Older Adult (100+)'),
        ('Older Adult (90-94)', 'Older Adult (90-94)'),
        ('Choose not to share', 'Choose not to share')
    )
    
    family_member_id = models.OneToOneField(FamilyMember, null=False, on_delete=models.CASCADE)
    age_range = models.CharField(max_length=255, null=True, choices=AGE_RANGE)

    def __str__(self):
        """Label as Family # | Member #."""
        return str(self.family_member_id) + ' | Age Range'
