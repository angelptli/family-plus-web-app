from django.shortcuts import render
from languages.models import LanguageSpecifier
from languages.utils import create_lang_db, get_lang_field_names

def welcome(request, *args, **kwargs):
    """Render requests for the welcome page."""
    context = {}
    
    # Automate language db creation on first visit to welcome page
    # if none found
    if not LanguageSpecifier.objects.count():
        create_lang_db()

    lang_mod = LanguageSpecifier.objects.get(language_mod="Language DB1")
    context['lang_mod'] = lang_mod

    # List of language field names
    lang_list = []
    lang_list = get_lang_field_names()[2:]
    context['lang_list'] = lang_list

    # List of language fields with their verbose names
    # Credit https://stackoverflow.com/questions/14496978/fields-verbose-name-in-templates
    lang_vlist = []
    lang_vlist = [lang_mod._meta.get_field(lang_field).verbose_name for lang_field in lang_list] 
    context['lang_vlist'] = lang_vlist

    # Get list of selected languages
    selected_languages = []
    selected_languages = request.POST.getlist("selected_languages")
    context['selected_languages'] = selected_languages
    
    return render(request, 'home_page/welcome.html', context)


def home(request):
    """Render requests for home page."""
    return render(request, 'home_page/home.html', {})


def about_view(request, *args, **kwargs):
    """Pending requests page view."""
    return render(request, 'general_info/about.html', {})


def faq_view(request, *args, **kwargs):
    """Pending requests page view."""
    return render(request, 'general_info/faq.html', {})