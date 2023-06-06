from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=200)  
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField
    articles = models.ManyToManyField
    comments = models.ManyToManyField

    def __init__(self, userName, userEmail, password, is_admin, article, comment):
        self.userName = userName
        self.userEmail = userEmail
        self.password = password
        self.is_admin = is_admin
    
    def connect(self, userName, password):
        pass

    def create_article(self, title, content, image, video):
        article = Article(title, content, image, video)
        article.save()
        return article
    
    def edit_article():
        pass

    def delete_article():
        pass

    def create_comment(self, content, title):
        comment = Comment(content)
        return comment

    def edit_comment():
        pass

    def delete_comment():
        pass

    def __str__(self):
         return self.userName + ' ' + self.userEmail

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField
    author = User
    image = models.ImageField(upload_to="chemin vers fichier")
    video = models.FileField(upload_to='chemin')
    is_published = models.BooleanField
    created_at = models.DateTimeField('date published')
    update_at = models.DateTimeField('date update')

class Comment(models.Model):
    content = models.CharField(max_length=300)
    author = User
