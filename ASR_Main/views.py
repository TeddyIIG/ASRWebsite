from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import UserSignupForm


# Create your views here.

def main(request):
    return render(request, 'MainClient/main.html')


def underconstruction(request):
    return render(request, 'MainClient/underconstruction.html')


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.clienttype = form.cleaned_data.get('clienttype1')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.phoneno = form.cleaned_data.get('phonenumber1')
            user.save()
            user.profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('main')
    else:
        form = UserSignupForm()
    return render(request, 'MainClient/signup.html', {'form': form})
