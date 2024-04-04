from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Message(models.Model):
    message = models.CharField(max_length=140, verbose_name='Mensaje')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicación')
