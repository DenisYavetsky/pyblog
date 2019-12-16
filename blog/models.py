from django.db import models
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField

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
    #body = models.TextField(blank=True)
    body = RichTextUploadingField(blank=True)
    date_pub = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField('Category', blank=True, related_name='posts')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    img = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})

