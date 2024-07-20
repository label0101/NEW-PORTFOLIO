from django.contrib import admin
from .models import Contact
from django.utils.html import format_html

# Register your models here.


@admin.register(Contact)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    
