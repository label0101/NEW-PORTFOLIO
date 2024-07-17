from django.shortcuts import render
from .models import About , Books,Contact,Index,Portfolio,Gallery
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator

import math
def index_view(request):
 return render(request,'index.html')

def about_view(request):
 return render(request,'about.html')

def books_view(request):
 return render(request,'books.html')

def contact_view(request):
 return render(request,'contact.html')

def portfolio_view(request):
 return render(request, 'portfolio.html')


def gallery_view(request):
 return render(request, 'gallery.html')


def blog_view(request):
 return render(request, 'blog.html')
