from django.shortcuts import render, HttpResponse


# Create your views here.

def main(request):
    return render(request, 'MainClient/main.html')
