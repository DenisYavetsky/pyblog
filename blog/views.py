from django.shortcuts import render
from .models import Post, Tag, Category, Faq, ContactForm
from django.shortcuts import get_object_or_404

#from django.core.mail import send_mail, BadHeaderError
#from django.http import HttpResponse
from django.core.mail import EmailMessage

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




