from django import forms

from .models import ratings


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=1000)  # dapp name
    text = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={"class": "form-control"}))
    rating = forms.ChoiceField(choices=ratings, widget=forms.RadioSelect())
