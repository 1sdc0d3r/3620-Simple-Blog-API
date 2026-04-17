from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from library.models import Author
from library.api.serializers import AuthorSerializer

@api_view(['GET', 'POST'])
# @api_view()
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
def author(req, id):
    try:
        author = Author.objects.get(pk=id)
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
