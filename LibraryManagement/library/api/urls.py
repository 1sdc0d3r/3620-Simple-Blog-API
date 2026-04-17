from django.urls import path, include
# from library.api.views import authors,author
from library.api.views import AuthorList,AuthorDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:id>', AuthorDetail.as_view(), name='author'),
    # path('books/', AuthorDetail.as_view(), name='author'),
    # path('books/<int:id>', AuthorDetail.as_view(), name='author'),
    # path('loans/', AuthorDetail.as_view(), name='author'),
    # path('loans/<int:id>', AuthorDetail.as_view(), name='author'),
]
