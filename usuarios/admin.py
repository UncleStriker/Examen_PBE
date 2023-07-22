from django.contrib import admin
from .models import User, Topico, Post

# Register your models here.


admin.site.register(User)
admin.site.register(Topico)
admin.site.register(Post)
