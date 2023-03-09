import datetime

from django.db import models

# Create your models here.


class Person(models.Model):
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} | | {self.email} | | {self.age}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='post_author', null=False, blank=False)

    def __str__(self):
        return f'{self.title} | | {self.created_at}'


class Comment(models.Model):
    text = models.CharField(max_length=255)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_on')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text} | | {self.author} | | {self.post}'


class Home(models.Model):
    text = models.TextField()
