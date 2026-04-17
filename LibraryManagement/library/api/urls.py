from django.urls import path, include
from library.api.views import get_authors

urlpatterns = [
    path('authors/', get_authors, name='authors'),
    # path('posts/<int:id>', blog_post, name='blog-post'),
]
