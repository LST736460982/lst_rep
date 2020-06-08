from django import forms
class Mail(forms.Form):
    subject=forms.CharField()
    message=forms.CharField()
    email=forms.EmailField()