from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, verbose_name='username')
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    is_active = models.BooleanField("Активен", default=True)
    is_staff = models.BooleanField("Персонал", default=False)
    data_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)
    last_online_date = models.DateTimeField("Дата последного входа", auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='user/profile_photo/')
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    description = models.TextField(verbose_name='Описание')

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.full_name
    
# class Subscriber(models.Model):
#     user = models.OneToOneField(Profile, name=)
#     user = models.OneToOneField(Profile, name='user_in_')