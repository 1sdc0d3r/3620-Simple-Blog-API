from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from library.api.views import authors,author
from library.api.views import AuthorList,AuthorDetail,BookList,BookDetail,LoanListVS
# LoanList,LoanDetail

router = DefaultRouter()
router.register('loans', LoanListVS, basename='loans_base')

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('', include(router.urls)),
    # path('loans/', LoanList.as_view(), name='loan-list'),
    # path('loans/<int:pk>', LoanDetail.as_view(), name='loan-detail'),

]
