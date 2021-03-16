from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'pages/home.html')


def contact(request):
    return render(request, 'pages/contact.html')


def error404(request, exception):
    return render(request, 'pages/error404.html', {'message': exception})


def error500(request):
    return render(request, 'pages/error500.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})
