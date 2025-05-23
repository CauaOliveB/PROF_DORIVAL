from django.shortcuts import render
from django.http import HttpResponse

def ola(request):
    return HttpResponse("Olá, DS14!!!")