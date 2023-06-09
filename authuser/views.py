from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User, Article, Comment
from .serializers import UserSerializer, ArticleSerializer, CommentSerializer
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

"""view all users datas"""

@api_view(['GET'])
def getUsers(request):
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
    success = False

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
    success = False

    users = User.objects.filter(email = data['email']).only() # fetch one user by email
    for user in users:
        password = data['password']
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
    success = False
    print(request.session['email'])
    try:
        del request.session['email'] # clear session
        del request.session['is_admin']
        del request.session['id_user']
        del request.session['id_user_art']
        success = True
    except KeyError:
        pass

    return Response({'success': success, 'error': None})

"""add new article"""

@api_view(['POST'])
def add(request):
    data = request.data
    error = None
    success = False
    # title = data['title']
    # description = data['description']
    # url_image = data['url_image']
    try:
        data['author'] = request.session['email']
        data['id_user'] = request.session['id_user']
    except Exception as e:
        error = 'login'
        return Response({'success': success, 'error': error})

    serializer = ArticleSerializer(data=data)

    if serializer.is_valid():
        try:
            serializer.save()
            success = True
        except Exception as  e:
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
    error = None
    try:
        article = Article.objects.get(pk=article_id)
        request.session['id_user_art'] = article.id_user.id # id of the user who owns the item

        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    except Exception as e:
        error = e

    return Response({'success': False, 'error': error})
    
"""delete article"""

@api_view(['GET'])
def delete_article(request, article_id):

    error = None
    success = False

    if request.session['id_user_art'] == request.session['id_user']  or request.session['is_admin']:
        try:
            article = Article.objects.get(pk=article_id)
            article.delete()
            success = True
        except Exception as e:
            error = e
            success = False
    
    return Response({'success': success, 'error': error})

"""update article"""

@api_view(['POST'])
def update_article(request, article_id):
    data = request.data
    # data['id'] = article_id
    # data['author'] = request.session['email']
    # data['id_user'] = request.session['id_user']
    error = None
    success = False

    # serializer = ArticleSerializer(data=data)

    # if serializer.is_valid():
    #     try:
    #         serializer.save()
    #         success = True
    #     except Exception as e:
    #         error = "Modification echouée"
    
    if request.session['id_user_art'] == request.session['id_user']:
        try:
            article = Article.objects.get(pk=article_id)
            article.title = data['title']
            article.description = data['description']
            article.url_image = data['url_image']
            # update at
            article.save()
            success = True
        except Exception as e:
            error = "failed"
            print(e)

    return Response({'success': success, 'error': error})

"""add comment"""

@api_view(['POST'])
def add_comment(request, article_id):

    data = request.data
    error = None
    success = False
    # body = data['body']
    try:
        data['author'] = request.session['email']
        data['id_user'] = request.session['id_user']
        data['id_article'] = article_id
    except:
        error = 'none article'
    
    serializer = CommentSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        success = True
    
    return Response({'success': success, 'error': error})

"""view all article comments"""

@api_view(['GET'])
def view_all_comments(request, article_id):
    error = None
    try:
        comments = Comment.objects.filter(id_article=article_id).all()
        serializer = CommentSerializer(comments, many=True)
    except Exception as e:
        error = "error"
        return Response({'error': error})

    return Response(serializer.data)

"""update comment"""

@api_view(['POST'])
def update_comment(request, article_id, comment_id):
    data = request.data
    body = data['body']
    error = None
    success = False
    
    try:
        comment = Comment.objects.get(pk= comment_id ,id_article = article_id)
    except Exception as e:
        error = "You cannot edit this comment !"
        print(e)
        return Response({'success': success, 'error': error})
    
    if  article_id == request.session['id_user_art'] and comment.id_user.id == request['id_user']:
        comment.body = body
        comment.save()
        success = True
    else:
        return Response({'success': success, 'error': error})
    
    return Response(comment)

"""delete comment """

@api_view(['GET'])
def delete_comment(request, article_id, comment_id):
    error = None
    success = False
    
    try:
        comment = Comment.objects.get(pk= comment_id ,id_article = article_id)
    except Exception as e:
        error = "You cannot delete this comment !"
        print(e)
        return Response({'success': success, 'error': error})
    
    if  article_id == request.session['id_user_art'] and comment.id_user.id == request['id_user']:
        comment.delete()
        success = True
    else:
        return Response({'success': success, 'error': error})
    
    return Response(comment)
