from django.urls import path
from authuser import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('signup/', views.signup, name='postData'),
    path('login/', views.login, name='login'),
    path('add/', views.add, name='add'),
    path('logout/', views.logout, name='logout'),
    path('fil/', views.get_published_article, name='get_published_article'),
    path('fil/<int:article_id>/', views.view_article, name='view_article'),
    path('fil/<int:article_id>/delete/', views.delete_article, name='view_article'),
    path('fil/<int:article_id>/update/', views.update_article, name='view_article'),
    path('fil/<int:article_id>/comment/', views.update_article, name='view_article')
]