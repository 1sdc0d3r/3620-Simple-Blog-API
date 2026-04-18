from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status
from library.models import Author, Book, Loan
from library.api.serializers import AuthorSerializer, BookSerializer, LoanSerializer

class AuthorList(APIView):
    def get(self,req):
        authors = Author.objects.all()
        cereal = AuthorSerializer(authors, many=True)
        return Response(cereal.data)

    def post(self,req):
        cereal = AuthorSerializer(data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):
    def get(self,req,pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = AuthorSerializer(author)
        return Response(cereal.data)

    def put(self,req,pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = AuthorSerializer(author, data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_200_OK)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,req,pk):
        try:
            author = Author.objects.get(pk=pk)
        except:
            return Response({'Error': "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookList(APIView):
    def get(self,req):
        books = Book.objects.all()
        cereal = BookSerializer(books, many=True, context={'request': req})
        return Response(cereal.data)

    def post(self,req):
        cereal = BookSerializer(data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get(self,req,pk):
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = BookSerializer(book, context={'request': req})
        return Response(cereal.data)

    def put(self,req,pk):
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = BookSerializer(book, data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_200_OK)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,req,pk):
        try:
            book = Book.objects.get(pk=pk)
        except:
            return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoanList(APIView):
    def get(self,req):
        loans = Loan.objects.all()
        cereal = LoanSerializer(loans, many=True, context={'request': req})
        return Response(cereal.data)

    def post(self,req):
        cereal = LoanSerializer(data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetail(APIView):
    def get(self,req,pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except:
            return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = LoanSerializer(loan, context={'request': req})
        return Response(cereal.data)

    def put(self,req,pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except:
            return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        cereal = LoanSerializer(loan, data=req.data)
        if cereal.is_valid():
            cereal.save()
            return Response(cereal.data, status=status.HTTP_200_OK)
        else:
            return Response(cereal.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,req,pk):
        try:
            loan = Loan.objects.get(pk=pk)
        except:
            return Response({'Error': "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
