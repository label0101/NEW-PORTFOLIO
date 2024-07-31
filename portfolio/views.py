from django.shortcuts import render
from .models import Contact,Portfolio,PortfolioCategory
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.generic.edit import FormView
from .bot import send_message
from django.views.generic.list import ListView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        content = form.cleaned_data.get('content')
        text = f"Name: {name}\nEmail: {email}\ntext: {content}"
        send_message(text)
        

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


# def portfolio_view(request):
#  return render(request, 'portfolio.html')
class PortfolioListView(ListView):
    model = Portfolio
    # paginate_by = 100  # if pagination is desired
    context_object_name = 'portfolios'
    template_name = "portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context

def gallery_view(request):
 return render(request, 'gallery.html')


def blog_view(request):
 return render(request, 'blog.html')
