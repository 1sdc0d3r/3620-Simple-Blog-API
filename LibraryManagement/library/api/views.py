# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from blog_app.models import Blog
# from blog_app.api.serializers import BlogSerializer

# @api_view()
# def blog_posts(req):
#     posts = Blog.objects.all()
#     bs = BlogSerializer(posts, many=True)
#     return Response(bs.data)

# @api_view()
# def blog_post(req, id):
#     post = Blog.objects.get(pk=id)
#     bs = BlogSerializer(post)
#     return Response(bs.data)
