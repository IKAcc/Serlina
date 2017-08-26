from django.contrib.auth.models import User
from django.db import models


class BlogPost(models.Model):
    """
    Store blog post information
    """

    title = models.CharField("post title", max_length = 100)
    content = models.TextField("post content")
    author = models.Foreignkey(User, on_delete = models.CASCADE)
    date_publish = models.DateTimeField(auto_now_add = True, blank = True)
    # comment add later
    category = models.Foreignkey(BlogCategory, on_delete = models.CASCADE)
    tags = models.Foreignkey(BlogTag, on_delete = models.CASCADE)


class BlogCategory(models.Model):
    """Store category
    each post could choosen one any category. :model: Blog.models.BlogCategory
    related to :model: Blog.models.BlogPost
    """

    cat_name = models.CharField("post category", max_length = 120)


class BlogTag(models.Model):
    """Store tags
    each post could choosen any tag. :model: Blog.models.BlogTag
    related to :model: Blog.models.BlogPost
    """

    tag_name = models.CharField("tags", max_length = 80)


############# needs for, added comment and blog user models
