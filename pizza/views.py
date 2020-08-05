from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')
