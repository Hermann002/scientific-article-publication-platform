from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=30)
    userEmail = models.CharField(max_length=200)  
    password = models.CharField(max_length=20)
    is_admin = False
    articles = models.ManyToManyField
    comments = models.ManyToManyField

    def __unicode__(self, userName, userEmail, password):
        self.userName = userName
        self.userEmail = userEmail
        self.password = password
    
    def connect(self, userName, password):
        pass

    def create_article(self, title, content, image, video):
        article = Article(title, content,  image, video, author = self.userName)
        article.save()

        return article
    
    def get_is_admin(self):
        return self.is_admin
    
    def set_is_admin(self, status):
        self.is_admin = status
    
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
    is_published = False
    created_at = models.DateTimeField('date published')
    update_at = models.DateTimeField('date update')

    def __artcode__(self, title, content, image, video):
        self.title = title
        self.content = content
        self.image = image
        self.video = video
    
    def get_is_published(self):
        return self.is_published
    
    def set_is_published(self, status):
        self.is_published = status

class Comment(models.Model):
    content = models.CharField(max_length=300)
    author = User
