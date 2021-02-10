from django.shortcuts import render
from .models import Post, Tag, Category, Faq, ContactForm, PostLikes, PostCountViews, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.shortcuts import redirect

from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
import random


def addlike(request, slug):
    session_key = request.session.session_key
    likes = PostLikes.objects.filter(sessionId=session_key)
    post = get_object_or_404(Post, slug__iexact=slug)  # возвращает id статьи или 404.
    post.like_count += 1  # Прибавляет единицу к article_likes
    post.save()  # сохраняет
    return HttpResponseRedirect('/')  # делает редирект на ту же страницу


def faq(request):
    faqs = Faq.objects.all()
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'faq.html', context={'faqs': faqs, 'posts': posts, 'tags': tags, 'categories': categories})


def contacts(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']

            #try:
            #    send_mail(subject, message, sender, ['yavetsky@gmail.com'],)
            #except BadHeaderError:  # Защита от уязвимости
            #    return HttpResponse('Invalid header found')
            # Переходим на другую страницу, если сообщение отправлено
            try:
                email = EmailMessage(subject, 'From: ' + sender + '\n' + message, to=['yavetsky@gmail.com'], reply_to=[sender])
                email.send()
            except:
                pass

            return render(request, 'mailsend.html', context={'posts': posts, 'tags': tags, 'categories': categories})
    else:
        form = ContactForm()
        # Отправляем форму на страницу
    return render(request, 'contacts.html', context={'posts': posts, 'tags': tags, 'categories': categories, 'form': form})


def posts_list(request):
    posts = Post.objects.all().order_by('-date_pub')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    return render(request, 'main.html', context={'posts': posts, 'tags': tags, 'categories': categories})


def post_detail(request, slug):

    c_form = CommentForm()
    # Получаем все теги и категории для бокового меню
    tags = Tag.objects.all()
    categories = Category.objects.all()

    # Проверяем есть ли пост с запрашиваемым слагом
    post = get_object_or_404(Post, slug__iexact=slug)
    comments = Comment.objects.filter(post=post.id)

    #делаем защиту от ботов
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    math_res = a + b

    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            if int(request.POST['check_sum']) == math_res:
                if request.POST['name'] not in ['teahGackpeta', 'FurneInosse', 'TiceDuesite', 'excelaysuelapaw', 'excelaysuelapaw', 'Sypepalsslato']:
                    Comm = c_form.save(commit=False)
                    Comm.post = post
                    Comm.save()
                    post.comment_count = comments.count()
                    post.save()
            return redirect(request.path)

    if not request.session.session_key:
        request.session.save()
    # получаем сессию
    session_key = request.session.session_key
    # если пост найден проверяем есть ли у него просмотры по id поста и sesId
    is_views = PostCountViews.objects.filter(postId=post.id, sesId=session_key)

    # если нет информации о просмотрах создаем ее
    if is_views.count() == 0 and str(session_key) != 'None':

        views = PostCountViews()
        views.sesId = session_key
        views.postId = post
        views.save()

        post.count_views += 1
        post.save()

    return render(request, 'post_detail.html', context={'post': post, 'tags': tags, 'categories': categories, 'comments': comments, 'c_form': c_form, 'protect': [a, b]})






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




