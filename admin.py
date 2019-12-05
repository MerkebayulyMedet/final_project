from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Statistic)
admin.site.register(Article)
admin.site.register(Course)
admin.site.register(Author)
admin.site.register(Comment)
