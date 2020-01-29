from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 4

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

def AboutPageView(request):
    return render(request, 'about.html')

def ContactPageView(request):
    return render(request, 'contact.html')

