from django.urls import path
from blog import views


urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),
    path('post/<str:slug>/', views.post_detail, name='post_detail_url'),
    path('category/<str:slug>/', views.category_detail, name='category_detail_url'),
    path('tag/<str:slug>/', views.tag_detail, name='tag_detail_url'),

]

