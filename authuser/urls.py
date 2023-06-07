from django.urls import path
from authuser import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('add/', views.postdata, name='postData')
]