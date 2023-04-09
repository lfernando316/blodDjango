from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
# Create your views here.

class BlogListView(APIView):
    def get(self, request, *args, **kwargs):
        post = Post.postobjects.all()[0:4]

        serializer = PostSerializer(posts,many=True)

        return Response(serializer.data) 

class PostDetailView(APIView):
    def get(self, request, post_slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=post_slug)

        serializer = PostSerializer(posts)

        return Response(serializer.data) 
