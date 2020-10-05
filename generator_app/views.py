from django.shortcuts import render

import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters=list('absdefghijklmnopqrstyuvwz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUYVW'))
    if request.GET.get('number'):
        characters.extend(list('123456789'))
    if request.GET.get('symbols'):
        characters.extend(list('!@#$%^&*()<>?}{]['))
    length = int(request.GET.get('length'))
    thepassword = ''
    for x in range( length ):
        thepassword+=random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})

