from django import forms

class ItemForm(forms.Form):
    item = forms.CharField(label="Item Input", max_length=25)