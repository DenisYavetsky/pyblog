from django.urls import path, include
from blog import views
from django.conf import settings
from django.views.static import serve

from django.conf.urls.static import static


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.posts_list, name='posts_list_url'),
    path('posts/', views.posts_list, name='posts_list_url'),
    path('faq/', views.faq, name='faq_url'),
    path('contacts/', views.contacts, name='contacts_url'),
    path('post/addlike/<str:slug>/', views.addlike, name='addlike'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    #path('faq/<str:slug>/', views.faq, name='faq_url'),
    path('category/<str:slug>/', views.category_detail, name='category_detail_url'),
    path('tag/<str:slug>/', views.tag_detail, name='tag_detail_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    urlpatterns += [
        path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

