from rest_framework import serializers

from Blog.models import BlogCategory, BlogTag, BlogPost, BlogComment, BlogInteracter
from django.contrib.auth.models import User

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'cat_name')

class  BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = ('id', 'tag_name')

class BlogPostSerializer(serializers.ModelSerializer):

    category = BlogCategorySerializer(read_only = True, many = True)
    tags = BlogTagSerializer(many = True)
    author = AuthorSerializer(many = True)

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'content', 'author', 'date_publish', 'category', 'tags')

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ('id', 'comment_content', 'related_post', 'comment_date', 'comment_reply')

class BlogInteracterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogInteracter
        fields = ('id', 'name', 'family', 'email', 'comment')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
