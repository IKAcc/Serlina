from Blog.models import BlogCategory
from Blog.serializers import BlogCategorySerializer
from rest_framework import generics


class BlogCategoryList(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
