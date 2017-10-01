from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from Blog import views

urlpatterns = [
    #/categories/
    url(r'^categories/', views.CategoryListView.as_view()),
    #/edit_category/
    url(r'^edit_category/(?P<pk>[0-9+])/', views.UpdateCategoryView.as_view()),
    #/tags/
    url(r'^tag/', views.TagListView.as_view()),
    # /edit_tag/
    url(r'^edit_tag/(?P<pk>[0-9+])/', views.UpdateTagView.as_view()),
    #/add_post/
    url(r'add_post/', views.AddPostView.as_view()),
    #/edit_post/
    url(r'edit_post/(?P<pk>[0-9]+)/', views.UpdatePostView.as_view()),
    #/post_list/
    url(r'post_list/', views.BlogPostLitView.as_view()),
]
