from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User, Article
from .serializers import UserSerializer, ArticleSerializer
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

"""view all users datas"""

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

"""allow user to register in the plateforme"""

@api_view(['POST'])
def signup(request):
    data = request.data
    password = data['password']
    data['password'] = make_password(password) # hash password
    serializer = UserSerializer(data=data)
    error = None
    success = None

    if serializer.is_valid():
        try:
            serializer.save()
            success = True
        except Exception as  e:
            error = e
            success = False
    
    return Response({'success': success, 'error': error})

"""allow users to login"""

@api_view(['POST'])
def login(request):
    data = request.data
    error = None
    success = None

    users = User.objects.filter(email = data['email']).only() # fetch one user by email
    for user in users:
        password = data['password']
        print('check password ...')
        if user is None:
            error = 'user is not registered'
            success = False
        elif not check_password(password, user.password):
            error = 'password incorrect'
            success = False
        else:
            success = True

        # set up cookies

        request.session['email'] = user.email
        request.session['is_admin'] = user.is_staff
        request.session['id_user'] = user.id
        response = Response({'success': success, 'error': error})
        # response.set_cookie('username', user.email)
    return response

"""logout and clear session"""

@api_view(['GET'])
def logout(request):
    try:
        del request.session # clear session
    except KeyError:
        pass
    return Response({'success': True, 'error': None})

"""add new article"""

@api_view(['POST'])
def add(request):
    data = request.data
    title = data['title']
    description = data['description']
    url_image = data['url_image']
    email = request.session['email']
    id_user = request.session['id_user']
    error = None
    success = False

    try:
        article = Article(title, description, url_image, email, id_user)
        article.save()
        success = True
    except Exception as e:
        error = e
        success = False

    return Response({'success': success, 'error': error})

"""access news feed"""

@api_view(['GET'])
def get_published_article(request):
    try:
        del request.session['id_user_art'] # delete session because it will be reset when accessing an article
    except KeyError:
        pass

    articles = Article.objects.filter(is_published = True).all()
    serializer = ArticleSerializer(articles, many = True)

    return Response(serializer.data)

"""view an article"""

@api_view(['GET'])
def view_article(request, article_id):
    article = Article.objects.filter(pk=article_id).only()
    for art in article:
        request.session['id_user_art'] = art.id_user.id

        serializer = ArticleSerializer(art)

        return Response(serializer.data)
    
