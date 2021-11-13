def define_age_ranges():
    """Return tuple of age ranges."""
    age_range_tuple = (
        ('On the way', 'On the way'),
        ('Baby (0-12 months old)', 'Baby (0-12 months old)'),
        ('Toddler (1-3 years old)', 'Toddler (1-3 years old)'),
        ('Preschooler (3-5 years old)', 'Preschooler (3-5 years old)'),
        ('Gradeschooler (5-12 years old)', 'Gradeschooler (5-12 years old)'),
        ('Teenager (12-17 years old)', 'Teenager (12-17 years old)'),
        ('Adult (18-24 years old)', 'Adult (18-24 years old)'),
        ('Adult (25-29 years old)', 'Adult (25-29 years old)'),
        ('Adult (30-34 years old)', 'Adult (30-34 years old)'),
        ('Adult (35-39 years old)', 'Adult (35-39 years old)'),
        ('Adult (40-44 years old)', 'Adult (40-45 years old)'),
        ('Adult (45-49 years old)', 'Adult (45-49 years old)'),
        ('Adult (50-54 years old)', 'Adult (50-54 years old)'),
        ('Adult (55-59 years old)', 'Adult (55-59 years old)'),
        ('Adult (60-64 years old)', 'Adult (60-64 years old)'),
        ('Older Adult (65-69 years old)', 'Older Adult (65-69 years old)'),
        ('Older Adult (70-74 years old)', 'Older Adult (70-74 years old)'),
        ('Older Adult (75-79 years old)', 'Older Adult (75-79 years old)'),
        ('Older Adult (80-84 years old)', 'Older Adult (80-84 years old)'),
        ('Older Adult (85-89 years old)', 'Older Adult (85-89 years old)'),
        ('Older Adult (90-94 years old)', 'Older Adult (90-94 years old)'),
        ('Older Adult (95-99 years old)', 'Older Adult (95-99 years old)'),
        ('Older Adult (100+ years old)', 'Older Adult (100+ years old)'),
        ('Baby', 'Baby'),
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Older Adult', 'Older Adult'),
        ('Senior', 'Senior'),
        ('Choose not to share', 'Choose not to share')
    )

    return age_range_tuple


def define_relations():
    """Return tuple of family relation placements."""
    relation_tuple = (
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Daughter', 'Daughter'),
        ('Son', 'Son'),
        ('Aunt', 'Aunt'),
        ('Uncle', 'Uncle'),
        ('Cousin', 'Cousin'),
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Foster Mother', 'Foster Mother'),
        ('Foster Father', 'Foster Father'),
        ('Foster Parent', 'Foster Parent'),
        ('Grandmother', 'Grandmother'),
        ('Grandfather', 'Grandfather'),
        ('Grandparent', 'Grandparent'),
        ('Relative', 'Relative'),
        ('Relative-In-Law', 'Relative-In-Law'),
        ('Family Friend', 'Family Friend'),
        ('Pet', 'Pet'),
        ('Other', 'Other'),
    )

    return relation_tuple