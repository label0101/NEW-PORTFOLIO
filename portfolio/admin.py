from django.contrib import admin
from .models import Contact,Portfolio, Blog, Category,Comment
from django.utils.html import format_html

# Register your models here.
admin.site.register((Comment,Category))

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','description')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category_name')

    def category_name(self, obj):
        return obj.category.name
    #rasmni ko'rinadigan qilasilar
