from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    
    charaters = list('abcdefghijklmnopqrstuvwxyz')
    length_of_password = int(request.GET.get('length', 12))  # 12 is like if we don't enter any length it will automatic generate 12 size password 

    if request.GET.get('uppercase'):
        charaters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charaters.extend(list('0123456789'))

    if request.GET.get('special'):
        charaters.extend(list('!@#$%^&*()'))


    secure_password = ""
    for i in range(length_of_password):
        secure_password += random.choice(charaters)

    return render(request, 'generator/password.html', {'password' : secure_password})


def about(request):
    return render(request, 'generator/about.html')