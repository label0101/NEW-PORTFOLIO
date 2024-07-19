from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView


class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


# def contact_view(request):
#  return render(request,'contact.html')


def index_view(request):
 return render(request,'index.html')

def about_view(request):
 return render(request,'about.html')

def books_view(request):
 return render(request,'books.html')


def portfolio_view(request):
 return render(request, 'portfolio.html')


def gallery_view(request):
 return render(request, 'gallery.html')


def blog_view(request):
 return render(request, 'blog.html')
