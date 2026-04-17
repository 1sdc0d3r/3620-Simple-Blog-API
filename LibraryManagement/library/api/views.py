from rest_framework.response import Response
from rest_framework.decorators import api_view
from library.models import Author
from library.api.serializers import AuthorSerializer

@api_view(['GET', 'POST'])
# @api_view()
def get_authors(req):
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


# @api_view()
# def blog_post(req, id):
#     post = Blog.objects.get(pk=id)
#     bs = BlogSerializer(post)
#     return Response(bs.data)
