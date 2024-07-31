from django.urls import path
from .views import index_view,books_view,PortfolioListView,about_view,gallery_view,blog_view,ContactFormView

urlpatterns = [
    path('',index_view,name='index-page'),
    path('contact/',ContactFormView.as_view(),name='contact-page'),
    path('books/',books_view,name='books-page'),
    path('portfolio/',PortfolioListView.as_view(),name='portfolio-page'),
    path('about/',about_view,name='about-page'),
    path('gallery/',gallery_view,name='gallery-page'),
    path('blog/',blog_view,name='blog-page'),
]
