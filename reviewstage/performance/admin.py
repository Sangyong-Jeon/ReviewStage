from django.contrib import admin
from .models import *

# Register your models here.

# SuperUser
# id : test01
# PW : test01

admin.site.register(Performance)
admin.site.register(Review)
admin.site.register(File)
admin.site.register(Bookmark)
