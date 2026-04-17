from rest_framework.response import Response
from rest_framework.decorators import api_view
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
                return Response(cereal.data)
            else:
                return Response(cereal.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def author(req, id):
    author = Author.objects.get(pk=id)
    match req.method:
        case 'GET':
            cereal = AuthorSerializer(author)
            return Response(cereal.data)

        case 'PUT':
            cereal = AuthorSerializer(author, data=req.data)
            if cereal.is_valid():
                cereal.save()
                return Response(cereal.data)
            else:
                return Response(cereal.errors)

        case 'DELETE':
            pass
