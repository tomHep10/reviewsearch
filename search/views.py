from django.shortcuts import render
from django.http import HttpResponse

def attribute(request):
    return render(request, 'reviewbot.html', {})