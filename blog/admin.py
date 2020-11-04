from django.contrib import admin
from .models import *


admin.site.register(Post)
admin.site.register(Faq)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(PostLikes)
admin.site.register(PostCountViews)
admin.site.register(Comment)