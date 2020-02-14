from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def main(request):
    return render(request, 'MainClient/main.html')


def signin(request):
    return render(request, 'MainClient/loginpage.html')


def signinuser(request):
    form = UserCreationForm()
    return render(request, 'MainClient/loginpage.html', {'form': form})


def underconstruction(request):
    return render(request, 'MainClient/underconstruction.html')

