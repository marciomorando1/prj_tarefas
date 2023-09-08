from django.shortcuts import render
from django.http import HttpResponse

def olamundo(request):
    return HttpResponse('Ola Mundo')
