from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"
    


# class About(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()

# class Books(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)

# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

# class Index(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()

# class Portfolio(models.Model):
#     project_name = models.CharField(max_length=100)
#     description = models.TextField()


# class Gallery(models.Model):
#     project_name = models.CharField(max_length=100)
#     description = models.TextField()
