from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(max_length=255, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    
# class Admin(User):
#     is_staff = models.BooleanField(default=True)

    
class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(default='')
    author = models.EmailField(blank=True, default='')
    url_image = models.CharField(default='', max_length=5000)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')

    #definir un constructeur pour la classe article
    def __artcode__(self, title, description, url_image, author, id_user):
        self.title = title
        self.description = description
        self.url_image = url_image
        self.author = author
        self.id_user = id_user
    
    def get_is_published(self):
        return self.is_published
    
    def set_is_published(self, status):
        self.is_published = status  

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField(default='', blank=False)
    author = models.EmailField(blank=True, default='')
    id_article = models.ForeignKey(to=Article, on_delete=models.CASCADE, default='')
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(default=timezone.now)

    def __comcode__(self, body, author, id_article, id_user):
        self.body = body
        self.author = author
        self.id_article = id_article
        self.id_user = id_user
