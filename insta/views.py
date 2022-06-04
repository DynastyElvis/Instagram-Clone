from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)



# Create your views here.

class PostListView(ListView):
    template_name = "insta/post_list.html"
    queryset = Post.objects.all()
    context_object_name = 'posts'
    
    
    
class PostCreateView(CreateView):
    template = 'insta/post_create.html'
    from_class = PostForm
