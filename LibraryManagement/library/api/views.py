from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import serializers, status, mixins, generics, viewsets
from library.models import Author, Book, Loan
from library.api.serializers import AuthorSerializer, BookSerializer, LoanSerializer

#! Concrete class views - most simple
# class ConcreteClassAuthorList(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self,req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

# class AuthorList(APIView):
#     def get(self,req):
#         authors = Author.objects.all()
#         cereal = AuthorSerializer(authors, many=True,context={'request': req})
#         return Response(cereal.data)

#     def post(self,req):
#         cereal = AuthorSerializer(data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)

    def put(self,req, *args, **kwargs):
        return self.update(req, *args, **kwargs)

    def delete(self,req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)



# class AuthorDetail(APIView):
#     def get(self,req,pk):
#         try:
#             author = Author.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = AuthorSerializer(author, context={'request': req})
#         return Response(cereal.data)

#     def put(self,req,pk):
#         try:
#             author = Author.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = AuthorSerializer(author, data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_200_OK)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,req,pk):
#         try:
#             author = Author.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BookList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self,req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

    def post(self,req, *args, **kwargs):
        return self.list(req, *args, **kwargs)

# class BookList(APIView):
#     def get(self,req):
#         books = Book.objects.all()
#         cereal = BookSerializer(books, many=True, context={'request': req})
#         return Response(cereal.data)

#     def post(self,req):
#         cereal = BookSerializer(data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self,req, *args, **kwargs):
        return self.retrieve(req, *args, **kwargs)

    def put(self,req, *args, **kwargs):
        return self.update(req, *args, **kwargs)

    def delete(self,req, *args, **kwargs):
        return self.destroy(req, *args, **kwargs)

# class BookDetail(APIView):
#     def get(self,req,pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = BookSerializer(book, context={'request': req})
#         return Response(cereal.data)

#     def put(self,req,pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = BookSerializer(book, data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_200_OK)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,req,pk):
#         try:
#             book = Book.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#* ViewSet replaces both LoanList and LoanListDetail
#* requires router in url's
#* ModelViewSet includes CRUD operations by default
class LoanListVS(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
'''
class LoanListVS(viewsets.ViewSet):
    def list(self, req):
        queryset = Loan.objects.all()
        cereal = LoanSerializer(queryset, many=True)
        return Response(cereal.data)

    def retrieve(self,req,pk=None):
        queryset = Loan.objects.all()
        loan = get_object_or_404(queryset, pk=pk)
        cereal = LoanSerializer(loan)
        return Response(cereal.data)

        #todo add post, update, delete
'''

# class LoanList(APIView):
#     def get(self,req):
#         loans = Loan.objects.all()
#         cereal = LoanSerializer(loans, many=True, context={'request': req})
#         return Response(cereal.data)

#     def post(self,req):
#         cereal = LoanSerializer(data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoanDetail(APIView):
#     def get(self,req,pk):
#         try:
#             loan = Loan.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = LoanSerializer(loan, context={'request': req})
#         return Response(cereal.data)

#     def put(self,req,pk):
#         try:
#             loan = Loan.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
#         cereal = LoanSerializer(loan, data=req.data)
#         if cereal.is_valid():
#             cereal.save()
#             return Response(cereal.data, status=status.HTTP_200_OK)
#         else:
#             return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self,req,pk):
#         try:
#             loan = Loan.objects.get(pk=pk)
#         except:
#             return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
#         loan.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'''
@api_view(['GET', 'POST'])
def authors(req):
    match req.method:
        case 'GET':
            authors = Author.objects.all()
            cereal = AuthorSerializer(authors, many=True)
            return Response(cereal.data)
        case 'POST':
            cereal = AuthorSerializer(data=req.data)
            if cereal.is_valid():
                cereal.save()
                return Response(cereal.data, status=status.HTTP_201_CREATED)
            else:
                return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author(req, pk):
    try:
        author = Author.objects.get(pk=pk)
    except:
        return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
    match req.method:
        case 'GET':
            cereal = AuthorSerializer(author)
            return Response(cereal.data)

        case 'PUT':
            cereal = AuthorSerializer(author, data=req.data)
            if cereal.is_valid():
                cereal.save()
                return Response(cereal.data, status=status.HTTP_200_OK)
            else:
                return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
'''
