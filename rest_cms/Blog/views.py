from rest_framework import generics

from Blog.models import BlogCategory, BlogTag, BlogPost
from Blog.serializers import BlogCategorySerializer, BlogTagSerializer, BlogPostSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class UpdateCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer

class TagListView(generics.ListCreateAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class UpdateTagView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class AddPostView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class UpdatePostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostLitView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
