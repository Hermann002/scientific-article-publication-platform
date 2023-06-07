from django.urls import path
from authuser import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('signup/', views.signup, name='postData'),
    path('login/', views.login, name='login')
]