from django.shortcuts import render


def home(request):
    """Render requests for home page."""
    return render(request, 'home_page/home.html', {})