from django import forms


class userInformations(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=30)
    your_email = forms.EmailField(label= "Your email", max_length=100)
    your_password = forms.PasswordInput