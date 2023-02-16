from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def main(request):
    return render(request, 'Home.html')

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'dangnhap.html')