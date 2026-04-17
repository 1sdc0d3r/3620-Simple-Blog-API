from django.urls import path, include
from library.api.views import authors,author

urlpatterns = [
    path('authors/', authors, name='authors'),
    path('authors/<int:id>', author, name='author'),
]
