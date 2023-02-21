from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *

# Create your views here.

def main(request):
    return render(request, 'Home.html')

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'dangnhap.html', context)