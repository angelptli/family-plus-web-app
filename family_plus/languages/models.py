from django.db import models
from django.conf import settings
from django.db.models.fields import TextField

class LanguageSpecifier(models.Model):
    # Language moderator set to store all language specifier data
    language_mod         = TextField(max_length=50, null=False, blank=False, default="Language DB")

    # 109 languages
    albanian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="albanian", verbose_name="Albanian")
    afrikaans            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="afrikaans", verbose_name="Afrikaans")
    amharic              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="amharic", verbose_name="Amharic")
    arabic               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="arabic", verbose_name="Arabic")
    armenian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="armenian", verbose_name="Armenian")
    azerbaijani          = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="azerbaijani", verbose_name="Azerbaijani")
    basque               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="basque", verbose_name="Basque")
    belarusian           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="belarusian", verbose_name="Belarusian")
    bengali              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="bengali", verbose_name="Bengali")
    bosnian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="bosnian", verbose_name="Bosnian")
    bulgarian            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="bulgarian", verbose_name="Bulgarian")
    catalan              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="catalan", verbose_name="Catalan")
    cebuano              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="cebuano", verbose_name="Cebuano")
    chewa                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="chewa", verbose_name="Chewa")
    chinese_simplified   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="chinese_simplified", verbose_name="Chinese (Simplified)")
    chinese_Traditional  = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="chinese_Traditional", verbose_name="Chinese (Traditional)")
    corsican             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="corsican", verbose_name="Corsican")
    croatian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="croatian", verbose_name="Croatian")
    czech                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="czech", verbose_name="Czech")
    danish               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="danish", verbose_name="Danish")
    dutch                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="dutch", verbose_name="Dutch")
    english              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="english", verbose_name="English")
    esperanto            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="esperanto", verbose_name="Esperanto")
    estonian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="estonian", verbose_name="Estonian")
    filipino_tagalog     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="filipino_tagalog", verbose_name="Filipino (Tagalog)")
    finnish              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="finnish", verbose_name="Finnish")
    french               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="french", verbose_name="French")
    frisian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="frisian", verbose_name="Frisian")
    galician             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="galician", verbose_name="Galician")
    georgian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="georgian", verbose_name="Georgian")
    german               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="german", verbose_name="German")
    greek                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="greek", verbose_name="Greek")
    gujarati             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="gujarati", verbose_name="Gujarati")
    haitian_creole       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="haitian_creole", verbose_name="Haitian Creole")
    hausa                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hausa", verbose_name="Hausa")
    hawaiian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hawaiian", verbose_name="Hawaiian")
    hebrew               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hebrew", verbose_name="Hebrew")
    hindi                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hindi", verbose_name="Hindi")
    hmong                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hmong", verbose_name="Hmong")
    hungarian            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="hungarian", verbose_name="Hungarian")
    icelandic            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="icelandic", verbose_name="Icelandic")
    igbo                 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="igbo", verbose_name="Igbo")
    indonesian           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="indonesian", verbose_name="Indonesian")
    irish                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="irish", verbose_name="Irish")
    italian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="italian", verbose_name="Italian")
    japanese             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="japanese", verbose_name="Japanese")
    javanese             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="javanese", verbose_name="Javanese")
    kannada              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="kannada", verbose_name="Kannada")
    kazakh               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="kazakh", verbose_name="Kazakh")
    khmer                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="khmer", verbose_name="Khmer")
    kinyarwanda          = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="kinyarwanda", verbose_name="Kinyarwanda")
    korean               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="korean", verbose_name="Korean")
    kurdish_Kurmanji     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="kurdish_Kurmanji", verbose_name="Kurdish (Kurmanji)")
    kyrgyz               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="kyrgyz", verbose_name="Kyrgyz")
    lao                  = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="lao", verbose_name="Lao")
    latin                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="latin", verbose_name="Latin")
    latvian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="latvian", verbose_name="Latvian")
    lithuanian           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="lithuanian", verbose_name="Lithuanian")
    luxembourgish        = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="luxembourgish", verbose_name="Luxembourgish")
    macedonian           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="macedonian", verbose_name="Macedonian")
    malagasy             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="malagasy", verbose_name="Malagasy")
    malay                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="malay", verbose_name="Malay")
    malayalam            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="malayalam", verbose_name="Malayalam")
    maltese              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="maltese", verbose_name="Maltese")
    maori                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="maori", verbose_name="Maori")
    marathi              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="marathi", verbose_name="Marathi")
    mongolian            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="mongolian", verbose_name="Mongolian")
    myanmar_burmese      = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="myanmar_burmese", verbose_name="Myanmar (Burmese)")
    nepali               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="nepali", verbose_name="Nepali")
    norwegian_bokmal     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="norwegian_bokmal", verbose_name="Norwegian (Bokmål)")
    odia                 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="odia", verbose_name="Odia")
    pashto               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="pashto", verbose_name="Pashto")
    persian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="persian", verbose_name="Persian")
    polish               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="polish", verbose_name="Polish")
    portuguese           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="portuguese", verbose_name="Portuguese")
    punjabi_gurmukhi     = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="punjabi_gurmukhi", verbose_name="Punjabi (Gurmukhi)")
    romanian             = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="romanian", verbose_name="Romanian")
    russian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="russian", verbose_name="Russian")
    samoan               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="samoan", verbose_name="Samoan")
    scottish_gaelic      = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="scottish_gaelic", verbose_name="Scottish Gaelic")
    serbian              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="serbian", verbose_name="Serbian")
    shona                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="shona", verbose_name="Shona")
    sindhi               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="sindhi", verbose_name="Sindhi")
    sinhala              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="sinhala", verbose_name="Sinhala")
    slovak               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="slovak", verbose_name="Slovak")
    slovenian            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="slovenian", verbose_name="Slovenian")
    somali               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="somali", verbose_name="Somali")
    sotho                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="sotho", verbose_name="Sotho")
    spanish              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="spanish", verbose_name="Spanish")
    sundanese            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="sundanese", verbose_name="Sundanese")
    swahili              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="swahili", verbose_name="Swahili")
    swedish              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="swedish", verbose_name="Swedish")
    tajik                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="tajik", verbose_name="Tajik")
    tamil                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="tamil", verbose_name="Tamil")
    tatar                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="tatar", verbose_name="Tatar")
    telugu               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="telugu", verbose_name="Telugu")
    thai                 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="thai", verbose_name="Thai")
    turkish              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="turkish", verbose_name="Turkish")
    turkmen              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="turkmen", verbose_name="Turkmen")
    ukrainian            = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="ukrainian", verbose_name="Ukrainian")
    urdu                 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="urdu", verbose_name="Urdu")
    uyghur               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="uyghur", verbose_name="Uyghur")
    uzbek                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="uzbek", verbose_name="Uzbek")
    vietnamese           = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="vietnamese", verbose_name="Vietnamese")
    welsh                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="welsh", verbose_name="Welsh")
    xhosa                = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="xhosa", verbose_name="Xhosa")
    yiddish              = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="yiddish", verbose_name="Yiddish")
    yoruba               = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="yoruba", verbose_name="Yoruba")
    zulu                 = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="zulu", verbose_name="Zulu")

    def __str__(self):
        return "Language"