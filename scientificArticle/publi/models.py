from django.db import models
import datetime

class User(models.Model):
    userName = models.CharField(max_length=30, unique= False)
    userEmail = models.CharField(max_length=200, unique= True)  
    password = models.CharField(max_length=20)
    is_admin = False
    articles = models.ManyToManyField
    comments = models.ManyToManyField

    #definir le constructeur
    def __unicode__(self, userName, userEmail, password):
        self.userName = userName
        self.userEmail = userEmail
        self.password = password
    
    def connect(self):
        pass

    # créer un article
    def create_article(self, title, description, image):
        article = Article(title, description, image, author = self.userName)
        article.save()

        return self.articles.append(article)
    
    def get_is_admin(self):
        return self.is_admin
    
    def set_is_admin(self, status):
        self.is_admin = status
    
    def edit_article():
        pass

    def delete_article():
        pass

    def create_comment(self, content):
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
    description = models.TextField()
    author = User
    image = models.ImageField(upload_to='scientific')
    is_published = False
    created_at = models.DateTimeField('date published')

    #definir un constructeur pour la classe article
    def __artcode__(self, title, description, image, author, create_at):
        self.title = title
        self.description = description
        self.image = image
        self.author = author
        self.created_at = create_at
    
    def get_is_published(self):
        return self.is_published
    
    def set_is_published(self, status):
        self.is_published = status


class Comment(models.Model):
    content = models.CharField(max_length=300)
    author = User
