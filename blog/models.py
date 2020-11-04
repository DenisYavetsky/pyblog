from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.shortcuts import reverse
from django import forms


class Tag(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})


class Post(models.Model):
    # название публикации
    title = models.CharField(max_length=150, db_index=True)
    # уникальный идентификатор
    slug = models.SlugField(max_length=150, unique=True)
    # счетчик просмотров
    count_views = models.IntegerField(default=0)
    # счетчик коментариев
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    # текст статьи
    body = RichTextUploadingField(blank=True)
    # дата публикации
    date_pub = models.DateField(auto_now_add=True)
    # к какому разделу относится статья
    categories = models.ManyToManyField('Category', blank=True, related_name='posts')
    # связанные теги для статьи
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    # изображение
    img = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['-date_pub']

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Faq(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = RichTextUploadingField(blank=True)
    date_pub = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('faq_url', kwargs={'slug': self.slug})


class ContactForm(forms.Form):
    '''форма обратной связи'''
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'back_form'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'back_form'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'back_form'}))


class PostLikes(models.Model):
    sessionId = models.CharField(default=True, max_length=128)
    postId = models.ForeignKey(Post, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.sessionId)


class PostCountViews(models.Model):
    # привязка к пользователю (сессии пользователя)
    sesId = models.CharField(max_length=150, db_index=True)
    # привязка к посту
    postId = models.ForeignKey(Post, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.sesId)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '{} {}'.format(self.name, self.text)
