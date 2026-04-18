from django.urls import path
# from library.api.views import authors,author
from library.api.views import AuthorList,AuthorDetail,BookList,BookDetail,LoanList,LoanDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='authors'),
    path('authors/<int:id>', AuthorDetail.as_view(), name='author'),
    path('books/', BookList.as_view(), name='author'),
    path('books/<int:id>', BookDetail.as_view(), name='author'),
    path('loans/', LoanList.as_view(), name='author'),
    path('loans/<int:id>', LoanDetail.as_view(), name='author'),
]
