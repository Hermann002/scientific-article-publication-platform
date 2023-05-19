from django import forms

class InfoUser(forms.Form):
    userName = forms.CharField(label="Your name", max_length=30)
    userEmail = forms.EmailField(label= "Your email", max_length=100)
    password = forms.CharField(label="password")