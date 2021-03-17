from django.shortcuts import render


def landing_page(request):
    return render(request, 'therealschool/landing_page.html', {})
