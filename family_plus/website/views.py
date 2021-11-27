from django.shortcuts import render
# from languages.models import LanguageSpecifier
# from languages.utils import create_lang_db, get_lang_field_names

def welcome(request, *args, **kwargs):
    """Render requests for the welcome page."""
    context = {}
    
    if request.user.is_authenticated:
        return render(request, 'home_page/home.html', context)
    else:
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