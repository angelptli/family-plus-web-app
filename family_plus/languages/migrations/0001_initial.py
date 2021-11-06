# Generated by Django 3.2.8 on 2021-11-05 01:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageSpecifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afrikaans', models.ManyToManyField(related_name='afrikaans', to=settings.AUTH_USER_MODEL)),
                ('albanian', models.ManyToManyField(related_name='albanian', to=settings.AUTH_USER_MODEL)),
                ('amharic', models.ManyToManyField(related_name='amharic', to=settings.AUTH_USER_MODEL)),
                ('arabic', models.ManyToManyField(related_name='arabic', to=settings.AUTH_USER_MODEL)),
                ('armenian', models.ManyToManyField(related_name='armenian', to=settings.AUTH_USER_MODEL)),
                ('azerbaijani', models.ManyToManyField(related_name='azerbaijani', to=settings.AUTH_USER_MODEL)),
                ('basque', models.ManyToManyField(related_name='basque', to=settings.AUTH_USER_MODEL)),
                ('belarusian', models.ManyToManyField(related_name='belarusian', to=settings.AUTH_USER_MODEL)),
                ('bengali', models.ManyToManyField(related_name='bengali', to=settings.AUTH_USER_MODEL)),
                ('bosnian', models.ManyToManyField(related_name='bosnian', to=settings.AUTH_USER_MODEL)),
                ('bulgarian', models.ManyToManyField(related_name='bulgarian', to=settings.AUTH_USER_MODEL)),
                ('catalan', models.ManyToManyField(related_name='catalan', to=settings.AUTH_USER_MODEL)),
                ('cebuano', models.ManyToManyField(related_name='cebuano', to=settings.AUTH_USER_MODEL)),
                ('chewa', models.ManyToManyField(related_name='chewa', to=settings.AUTH_USER_MODEL)),
                ('chinese_Traditional', models.ManyToManyField(related_name='chinese_Traditional', to=settings.AUTH_USER_MODEL)),
                ('chinese_simplified', models.ManyToManyField(related_name='chinese_simplified', to=settings.AUTH_USER_MODEL)),
                ('corsican', models.ManyToManyField(related_name='corsican', to=settings.AUTH_USER_MODEL)),
                ('croatian', models.ManyToManyField(related_name='croatian', to=settings.AUTH_USER_MODEL)),
                ('czech', models.ManyToManyField(related_name='czech', to=settings.AUTH_USER_MODEL)),
                ('danish', models.ManyToManyField(related_name='danish', to=settings.AUTH_USER_MODEL)),
                ('dutch', models.ManyToManyField(related_name='dutch', to=settings.AUTH_USER_MODEL)),
                ('english', models.ManyToManyField(related_name='english', to=settings.AUTH_USER_MODEL)),
                ('esperanto', models.ManyToManyField(related_name='esperanto', to=settings.AUTH_USER_MODEL)),
                ('estonian', models.ManyToManyField(related_name='estonian', to=settings.AUTH_USER_MODEL)),
                ('filipino_tagalog', models.ManyToManyField(related_name='filipino_tagalog', to=settings.AUTH_USER_MODEL)),
                ('finnish', models.ManyToManyField(related_name='finnish', to=settings.AUTH_USER_MODEL)),
                ('french', models.ManyToManyField(related_name='french', to=settings.AUTH_USER_MODEL)),
                ('frisian', models.ManyToManyField(related_name='frisian', to=settings.AUTH_USER_MODEL)),
                ('galician', models.ManyToManyField(related_name='galician', to=settings.AUTH_USER_MODEL)),
                ('georgian', models.ManyToManyField(related_name='georgian', to=settings.AUTH_USER_MODEL)),
                ('german', models.ManyToManyField(related_name='german', to=settings.AUTH_USER_MODEL)),
                ('greek', models.ManyToManyField(related_name='greek', to=settings.AUTH_USER_MODEL)),
                ('gujarati', models.ManyToManyField(related_name='gujarati', to=settings.AUTH_USER_MODEL)),
                ('haitian_creole', models.ManyToManyField(related_name='haitian_creole', to=settings.AUTH_USER_MODEL)),
                ('hausa', models.ManyToManyField(related_name='hausa', to=settings.AUTH_USER_MODEL)),
                ('hawaiian', models.ManyToManyField(related_name='hawaiian', to=settings.AUTH_USER_MODEL)),
                ('hebrew', models.ManyToManyField(related_name='hebrew', to=settings.AUTH_USER_MODEL)),
                ('hindi', models.ManyToManyField(related_name='hindi', to=settings.AUTH_USER_MODEL)),
                ('hmong', models.ManyToManyField(related_name='hmong', to=settings.AUTH_USER_MODEL)),
                ('hungarian', models.ManyToManyField(related_name='hungarian', to=settings.AUTH_USER_MODEL)),
                ('icelandic', models.ManyToManyField(related_name='icelandic', to=settings.AUTH_USER_MODEL)),
                ('igbo', models.ManyToManyField(related_name='igbo', to=settings.AUTH_USER_MODEL)),
                ('indonesian', models.ManyToManyField(related_name='indonesian', to=settings.AUTH_USER_MODEL)),
                ('irish', models.ManyToManyField(related_name='irish', to=settings.AUTH_USER_MODEL)),
                ('italian', models.ManyToManyField(related_name='italian', to=settings.AUTH_USER_MODEL)),
                ('japanese', models.ManyToManyField(related_name='japanese', to=settings.AUTH_USER_MODEL)),
                ('javanese', models.ManyToManyField(related_name='javanese', to=settings.AUTH_USER_MODEL)),
                ('kannada', models.ManyToManyField(related_name='kannada', to=settings.AUTH_USER_MODEL)),
                ('kazakh', models.ManyToManyField(related_name='kazakh', to=settings.AUTH_USER_MODEL)),
                ('khmer', models.ManyToManyField(related_name='khmer', to=settings.AUTH_USER_MODEL)),
                ('kinyarwanda', models.ManyToManyField(related_name='kinyarwanda', to=settings.AUTH_USER_MODEL)),
                ('korean', models.ManyToManyField(related_name='korean', to=settings.AUTH_USER_MODEL)),
                ('kurdish_Kurmanji', models.ManyToManyField(related_name='kurdish_Kurmanji', to=settings.AUTH_USER_MODEL)),
                ('kyrgyz', models.ManyToManyField(related_name='kyrgyz', to=settings.AUTH_USER_MODEL)),
                ('lao', models.ManyToManyField(related_name='lao', to=settings.AUTH_USER_MODEL)),
                ('latin', models.ManyToManyField(related_name='latin', to=settings.AUTH_USER_MODEL)),
                ('latvian', models.ManyToManyField(related_name='latvian', to=settings.AUTH_USER_MODEL)),
                ('lithuanian', models.ManyToManyField(related_name='lithuanian', to=settings.AUTH_USER_MODEL)),
                ('luxembourgish', models.ManyToManyField(related_name='luxembourgish', to=settings.AUTH_USER_MODEL)),
                ('macedonian', models.ManyToManyField(related_name='macedonian', to=settings.AUTH_USER_MODEL)),
                ('malagasy', models.ManyToManyField(related_name='malagasy', to=settings.AUTH_USER_MODEL)),
                ('malay', models.ManyToManyField(related_name='malay', to=settings.AUTH_USER_MODEL)),
                ('malayalam', models.ManyToManyField(related_name='malayalam', to=settings.AUTH_USER_MODEL)),
                ('maltese', models.ManyToManyField(related_name='maltese', to=settings.AUTH_USER_MODEL)),
                ('maori', models.ManyToManyField(related_name='maori', to=settings.AUTH_USER_MODEL)),
                ('marathi', models.ManyToManyField(related_name='marathi', to=settings.AUTH_USER_MODEL)),
                ('mongolian', models.ManyToManyField(related_name='mongolian', to=settings.AUTH_USER_MODEL)),
                ('myanmar_burmese', models.ManyToManyField(related_name='myanmar_burmese', to=settings.AUTH_USER_MODEL)),
                ('nepali', models.ManyToManyField(related_name='nepali', to=settings.AUTH_USER_MODEL)),
                ('norwegian_bokmal', models.ManyToManyField(related_name='norwegian_bokmal', to=settings.AUTH_USER_MODEL)),
                ('odia', models.ManyToManyField(related_name='odia', to=settings.AUTH_USER_MODEL)),
                ('pashto', models.ManyToManyField(related_name='pashto', to=settings.AUTH_USER_MODEL)),
                ('persian', models.ManyToManyField(related_name='persian', to=settings.AUTH_USER_MODEL)),
                ('polish', models.ManyToManyField(related_name='polish', to=settings.AUTH_USER_MODEL)),
                ('portuguese', models.ManyToManyField(related_name='portuguese', to=settings.AUTH_USER_MODEL)),
                ('punjabi_gurmukhi', models.ManyToManyField(related_name='punjabi_gurmukhi', to=settings.AUTH_USER_MODEL)),
                ('romanian', models.ManyToManyField(related_name='romanian', to=settings.AUTH_USER_MODEL)),
                ('russian', models.ManyToManyField(related_name='russian', to=settings.AUTH_USER_MODEL)),
                ('samoan', models.ManyToManyField(related_name='samoan', to=settings.AUTH_USER_MODEL)),
                ('scottish_gaelic', models.ManyToManyField(related_name='scottish_gaelic', to=settings.AUTH_USER_MODEL)),
                ('serbian', models.ManyToManyField(related_name='serbian', to=settings.AUTH_USER_MODEL)),
                ('shona', models.ManyToManyField(related_name='shona', to=settings.AUTH_USER_MODEL)),
                ('sindhi', models.ManyToManyField(related_name='sindhi', to=settings.AUTH_USER_MODEL)),
                ('sinhala', models.ManyToManyField(related_name='sinhala', to=settings.AUTH_USER_MODEL)),
                ('slovak', models.ManyToManyField(related_name='slovak', to=settings.AUTH_USER_MODEL)),
                ('slovenian', models.ManyToManyField(related_name='slovenian', to=settings.AUTH_USER_MODEL)),
                ('somali', models.ManyToManyField(related_name='somali', to=settings.AUTH_USER_MODEL)),
                ('sotho', models.ManyToManyField(related_name='sotho', to=settings.AUTH_USER_MODEL)),
                ('spanish', models.ManyToManyField(related_name='spanish', to=settings.AUTH_USER_MODEL)),
                ('sundanese', models.ManyToManyField(related_name='sundanese', to=settings.AUTH_USER_MODEL)),
                ('swahili', models.ManyToManyField(related_name='swahili', to=settings.AUTH_USER_MODEL)),
                ('swedish', models.ManyToManyField(related_name='swedish', to=settings.AUTH_USER_MODEL)),
                ('tajik', models.ManyToManyField(related_name='tajik', to=settings.AUTH_USER_MODEL)),
                ('tamil', models.ManyToManyField(related_name='tamil', to=settings.AUTH_USER_MODEL)),
                ('tatar', models.ManyToManyField(related_name='tatar', to=settings.AUTH_USER_MODEL)),
                ('telugu', models.ManyToManyField(related_name='telugu', to=settings.AUTH_USER_MODEL)),
                ('thai', models.ManyToManyField(related_name='thai', to=settings.AUTH_USER_MODEL)),
                ('turkish', models.ManyToManyField(related_name='turkish', to=settings.AUTH_USER_MODEL)),
                ('turkmen', models.ManyToManyField(related_name='turkmen', to=settings.AUTH_USER_MODEL)),
                ('ukrainian', models.ManyToManyField(related_name='ukrainian', to=settings.AUTH_USER_MODEL)),
                ('urdu', models.ManyToManyField(related_name='urdu', to=settings.AUTH_USER_MODEL)),
                ('uyghur', models.ManyToManyField(related_name='uyghur', to=settings.AUTH_USER_MODEL)),
                ('uzbek', models.ManyToManyField(related_name='uzbek', to=settings.AUTH_USER_MODEL)),
                ('vietnamese', models.ManyToManyField(related_name='vietnamese', to=settings.AUTH_USER_MODEL)),
                ('welsh', models.ManyToManyField(related_name='welsh', to=settings.AUTH_USER_MODEL)),
                ('xhosa', models.ManyToManyField(related_name='xhosa', to=settings.AUTH_USER_MODEL)),
                ('yiddish', models.ManyToManyField(related_name='yiddish', to=settings.AUTH_USER_MODEL)),
                ('yoruba', models.ManyToManyField(related_name='yoruba', to=settings.AUTH_USER_MODEL)),
                ('zulu', models.ManyToManyField(related_name='zulu', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]