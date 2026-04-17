from django.urls import path, include
from blog_app.views import blog_posts,blog_post

urlpatterns = [
    path('posts/', blog_posts, name='blog-posts'),
    path('posts/<int:id>', blog_post, name='blog-post'),
]
