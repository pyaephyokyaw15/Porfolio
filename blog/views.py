from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post
import markdown

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/blog-home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        print('Context', context)
        print(context['post'].body)
        context['body'] = markdown.markdown(context['post'].body, extensions=['fenced_code', 'sane_lists'])
        return context