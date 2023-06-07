from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

@api_view(['GET'])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def signup(request):
    data = request.data
    password = data['password']
    data['password'] = make_password(password)
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

@api_view(['POST'])
def login(request):
    data = request.data
    error = None
    success = None

    users = User.objects.filter(email = data['email']).only()
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

    return Response({'success': success, 'error': error})