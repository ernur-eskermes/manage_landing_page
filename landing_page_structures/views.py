from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FreeLessonForm


def landing_page(request):
    if request.POST:
        form = FreeLessonForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            subject = 'Здравствуйте!'
            message = '''Пройдите бесплатный урок
Оцените способ и формат подачи информации.
Узнайте вместе с ребёнком, что такое деньги и зачем нужна финансовая грамотность.'''
            send_mail(subject, message, from_email=None, recipient_list=[email])
            return HttpResponseRedirect('/')
    else:
        form = FreeLessonForm()
    return render(request, 'therealschool/landing_page.html', {'form': form})
