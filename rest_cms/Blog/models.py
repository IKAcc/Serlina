from django.contrib.auth.models import User
from django.db import models



class BlogCategory(models.Model):
    """Store category
    each post could choosen one any category. :model: Blog.models.BlogCategory
    related to :model: Blog.BlogPost
    """

    cat_name = models.CharField("post category", max_length = 120)


class BlogTag(models.Model):
    """Store tags
    each post could choosen any tag. :model: Blog.models.BlogTag
    related to :model: Blog.BlogPost
    """

    tag_name = models.CharField("tags", max_length = 80)


class BlogPost(models.Model):
    """
    Store blog post information
    """

    title = models.CharField("post title", max_length = 100)
    content = models.TextField("post content")
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    date_publish = models.DateTimeField(auto_now_add = True, blank = True)
    category = models.ForeignKey(BlogCategory, on_delete = models.CASCADE)
    tags = models.ForeignKey(BlogTag, on_delete = models.CASCADE)


class BlogComment(models.Model):
    """ Store user comment
    users could comment on each post but each comment belong to one post
    relared to :model: Blog.BlogPost
    """

    comment_content = models.CharField(max_length = 1000)
    related_post = models.ForeignKey(BlogPost, on_delete = models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    comment_reply = models.ForeignKey('self', on_delete = models.CASCADE, blank = True)


class BlogInteracter(models.Model):
    """Store information of users that comment on post
    related to :model: Blog.BlogComment
    """
    name = models.CharField(max_length = 40)
    family = models.CharField(max_length = 40)
    email = models.EmailField(max_length = 250)
    comment = models.ForeignKey(BlogComment, on_delete = models.CASCADE)
