from django.urls import path
# from library.api.views import authors,author
from library.api.views import AuthorList,AuthorDetail,BookList,BookDetail,LoanList,LoanDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('loans/', LoanList.as_view(), name='loan-list'),
    path('loans/<int:pk>', LoanDetail.as_view(), name='loan-detail'),
]
