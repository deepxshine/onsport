from django.shortcuts import render, get_object_or_404
from .models import Post, Categories


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    template = 'blog/index.html'
    return render(request, template, context)


def blog_list(request):
    categories = Categories.objects.all()
    context = {
        'categories': categories
    }
    template = 'blog/blog_list.html'
    return render(request, template, context)


def blog_category(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    posts = category.category.all()
    context = {
        'category': category,
        'posts': posts
    }
    template = 'blog/blog_category.html'
    return render(request, template, context)