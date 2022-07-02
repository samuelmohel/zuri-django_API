from atexit import register
from django.contrib import admin
from .models import Link



@admin.register(Link)
class Linkadmin(admin.ModelAdmin):
    pass
