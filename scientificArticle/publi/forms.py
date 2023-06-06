from django import forms

class InfoUser(forms.Form):
    userName = forms.CharField(label="Your name", max_length=30)
    userEmail = forms.EmailField(label= "Your email", max_length=100)
    password = forms.CharField(label="password")

class ArtDetail(forms.Form):
    title = forms.CharField(label="Entrer le titre de l'article", max_length=200)
    description = forms.CharField(label="Entrer une description")
    image = forms.ImageField(label="Entrer une image")
 