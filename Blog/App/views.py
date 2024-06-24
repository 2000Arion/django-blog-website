from typing import Any
from django.shortcuts import render

from .models import Post
from django.views import generic

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(Status=1).order_by("-Erstellt")
    template_name = "index.html"
    context_object_name = "post_list"
    
class DetailedView(generic.DetailView):
    model = Post
    template_name = "v.html"
    