from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import Contact


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Contact)
