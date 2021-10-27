from django.shortcuts import render


def welcome(request):
    """Render requests for the welcome page."""
    return render(request, 'home_page/welcome.html', {})


def home(request):
    """Render requests for home page."""
    return render(request, 'home_page/home.html', {})