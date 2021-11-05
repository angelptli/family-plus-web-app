from languages.models import LanguageSpecifier


def create_lang_db():
    """Create language db object if not found.
    
    This object is only created once and is initiated with the first visit
    to the welcome page. More can be created but only one is currently needed.
    """
    # Specify the language db name then create as an object
    language_db_name = "Language DB1"
    if not LanguageSpecifier.objects.count():
        LanguageSpecifier.objects.create(language_mod=language_db_name)


def get_lang_mod_obj():
    """Return language mod object that stores the language db data."""
    language_db_name = "Language DB1"
    obj = 0

    try:
        obj = LanguageSpecifier.objects.get(language_mod=language_db_name)
        return obj
    except LanguageSpecifier.DoesNotExist:
        return obj
        # # Or create db
        # create_lang_db()


def get_lang_field_names():
    """Return list of LanguageSpecifier field names.
    
    This function requires the holder variable to be initialized, e.g.
    lang_fields = [].
    
    After the variable can be assigned this function's returned list, e.g.
    lang_fields = get_lang_field_names()
    """
    language_fields = []
    language_fields = [field.name for field in LanguageSpecifier._meta.get_fields()]

    return language_fields


def get_languages_verbose(instance, field_name):
    """Return the object's verbose name."""
    # Credit https://stackoverflow.com/questions/14496978/fields-verbose-name-in-templates
    return instance._meta.get_field(field_name).verbose_name
