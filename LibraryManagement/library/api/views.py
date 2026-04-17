from rest_framework.response import Response
from rest_framework.decorators import api_view
from library.models import Author
from library.api.serializers import AuthorSerializer

@api_view()
def get_authors(req):
    authors = Author.objects.all()
    bs = AuthorSerializer(authors, many=True)
    return Response(bs.data)

# @api_view()
# def blog_post(req, id):
#     post = Blog.objects.get(pk=id)
#     bs = BlogSerializer(post)
#     return Response(bs.data)
