from django.contrib import admin
from .models import *
# Register your models here.

# SuperUser
# id : test01
# PW : test01

admin.site.register(Info)
admin.site.register(Review)

