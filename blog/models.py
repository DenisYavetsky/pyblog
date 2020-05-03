from django.db import models
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
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
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    count_views = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    body = RichTextUploadingField(blank=True)
    date_pub = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField('Category', blank=True, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    img = models.ImageField(upload_to='images/', blank=True)

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
    sesId = models.CharField(max_length=150, db_index=True)
    postId = models.ForeignKey(Post, blank=True, null=True, default=None, on_delete=models.CASCADE)
