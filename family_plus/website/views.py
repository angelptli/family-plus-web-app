from django.shortcuts import render


def welcome(request):
    """Render requests for the welcome page."""
    return render(request, 'home_page/welcome.html', {})


def home(request):
    """Render requests for home page."""
    return render(request, 'home_page/home.html', {})


def about_view(request, *args, **kwargs):
    """Pending requests page view."""
    return render(request, 'general_info/about.html', {})


def faq_view(request, *args, **kwargs):
    """Pending requests page view."""
    return render(request, 'general_info/faq.html', {})