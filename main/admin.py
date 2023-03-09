from django.contrib import admin

from main.models import Person, Post, Comment

# Register your models here.


admin.site.register(Person)
admin.site.register(Comment)
admin.site.register(Post)
