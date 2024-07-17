from django.urls import path
from .views import index_view,contact_view,books_view,portfolio_view,about_view,gallery_view,blog_view

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/',contact_view,name='contact-page'),
    path('books/',books_view,name='books-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('about/',about_view,name='about-page'),
    path('gallery/',gallery_view,name='gallery-page'),
    path('blog/',blog_view,name='blog-page'),
]
