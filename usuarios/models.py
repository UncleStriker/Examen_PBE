from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=11)


class Topico(models.Model):
    categoria = models.CharField(max_length=20)


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=144)
