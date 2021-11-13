# Generated by Django 3.2.8 on 2021-11-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0004_auto_20211112_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hobby',
            name='hobbies',
            field=models.CharField(choices=[('Amusement parks', 'Amusement parks'), ('Arts & crafts', 'Arts & crafts'), ('Baking', 'Baking'), ('Bicycling', 'Bicycling'), ('Board games', 'Board games'), ('Book club', 'Book club'), ('Bowling', 'Bowling'), ('Breadmaking', 'Breadmaking'), ('Camping', 'Camping'), ('Card games', 'Card games'), ('Carpentry', 'Carpentry'), ('Cooking', 'Cooking'), ('Creative writing', 'Creative writing'), ('Cultures', 'Cultures'), ('DIY Projects', 'DIY Projects'), ('Dance', 'Dance'), ('Decorating', 'Decorating'), ('Digital arts', 'Digital arts'), ('Dining', 'Dining'), ('Exercise', 'Exercise'), ('Handrawn art', 'Handrawn art'), ('Hiking', 'Hiking'), ('Farming', 'Farming'), ('Fashion', 'Fashion'), ('Fishing', 'Fishing'), ('Food', 'Food'), ('Houseplant care', 'Houseplant care'), ('Languages', 'Languages'), ('Lego building', 'Lego building'), ('Martial arts', 'Martial arts'), ('Math', 'Math'), ('Mechanics', 'Mechanics'), ('Media arts', 'Media arts'), ('Meditation', 'Meditation'), ('Music', 'Music'), ('Musical instruments', 'Musical instruments'), ('Nature', 'Nature'), ('Park activities', 'Park activities'), ('Performance arts', 'Performance arts'), ('Pet adoption & fostering', 'Pet adoption & fostering'), ('Pets', 'Pets'), ('Photography', 'Photography'), ('Physics', 'Physics'), ('Plants', 'Plants'), ('Poetry', 'Poetry'), ('Puzzles', 'Puzzles'), ('Reading', 'Reading'), ('Road trips', 'Road'), ('Science', 'Science'), ('Sports', 'Sports'), ('Video games', 'Video'), ('Volunteering', 'Volunteering'), ('Watching Movies', 'Watching Movies'), ('Watching Shows', 'Watching Shows'), ('Traveling', 'Traveling')], max_length=30, null=True),
        ),
    ]
