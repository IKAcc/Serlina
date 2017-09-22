from rest_framework import serializers
from blog.models import BlogCategory, BlogTag, BlogPost, BlogComment, BlogInteracter

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('id', 'cat_name')

class  BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTagSerializer
        fields = ('id', 'tag_name')

class BlogPostSerializer(serializers.ModelSerializer):
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
