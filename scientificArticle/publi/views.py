from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from publi.models import User, Article
from werkzeug.security import check_password_hash, generate_password_hash
from django.db import IntegrityError
import json


from .forms import InfoUser, ArtDetail

import datetime

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = request.POST 
        name = form['userName']
        email = form['userEmail']
        password = form['password']
        error = None

        if not name:
            error = 'User name required'
        elif not email:
            error = 'User email required'
        elif not password:
            error = 'password required'
            
        if error is None:
            try:
                user = User(userName=name , userEmail=email , password=generate_password_hash(password))
                user.save()
            except IntegrityError:
                error = f"l'utilisateur {name} existe déja !"
                response = {'valid': 0, "error": error}
                return HttpResponse(json.dumps(response))
            response = {'valid': 0}
            return HttpResponse(json.dumps(response))
        # check whether it's valid:
    # if a GET (or any other method) we'll create a blank form
    
        # recupérer la structure du formulaire dans fomrs.py
        # form = InfoUser() 
        # context = {"form":form}
    return HttpResponse('Vous devez utiliser la methode post')

def get_article(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ArtDetail(request.POST, request.FILES)
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES['image']

        article = Article.objects.create(image = image, description = description, title = title, created_at = datetime.datetime.now())

        article.save()

        # article_create = User.create_article(title, description, image)
        return HttpResponse(f'the name of uploaded file is {str(image)}')
    else:
        form = ArtDetail()
        context = {"form":form}
        # recupérer la structure du formulaire dans fomrs.py
        return render(request, "publi/inscArt.html", context)