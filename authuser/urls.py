from django.urls import path
from authuser import views

urlpatterns = [
    path('', views.getUsers, name='getData'),
    path('signup/', views.signup, name='postData'),
    path('login/', views.login, name='login'),
    path('add/', views.add, name='add'),
    path('logout/', views.logout, name='logout'),
    path('fil/', views.get_published_article, name='get_published_article'),
    path('fil/<int:article_id>/', views.view_article, name='view_article'),
    path('fil/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('fil/<int:article_id>/update/', views.update_article, name='update_article'),
    path('fil/<int:article_id>/comment/', views.add_comment , name='comment_article'),
    path('fil/<int:article_id>/comments/', views.view_all_comments, name='view_all_comments'),
    path('fil/<int:article_id>/update_comment/<int:comment_id>', views.update_comment, name='update_comment'),
    path('fil/<int:article_id>/delete_comment/<int:comment_id>', views.delete_comment, name='delete_comment')
]