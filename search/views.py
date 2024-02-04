from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def search(request):    
    if request.method == "POST":
        item = forms.ItemForm(request.POST)

        if item.is_valid():
            input = item.cleaned_data['item']
            print(input)
            return render(request, 'reviewbot.html', {'input':input})
    else:
        item = forms.ItemForm()
        return render(request, 'reviewbot.html', {'item':item})