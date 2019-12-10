from django.shortcuts import render
from .models import Post, Tag, Category
from django.shortcuts import get_object_or_404


def faq(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'faq.html', context={'posts': posts, 'tags': tags, 'categories': categories})


def contacts(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'contacts.html', context={'posts': posts, 'tags': tags, 'categories': categories})


def posts_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'main.html', context={'posts': posts, 'tags': tags, 'categories': categories})


def post_detail(request, slug):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'post_detail.html', context={'post': post, 'tags': tags, 'categories': categories})


def tag_detail(request, slug):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    tag = get_object_or_404(Tag, slug__iexact=slug)

    return render(request, 'tag_detail.html', context={'tag': tag, 'tags': tags, 'categories': categories})


def category_detail(request, slug):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug__iexact=slug)

    return render(request, 'category_detail.html', context={'category': category, 'tags': tags, 'categories': categories})

