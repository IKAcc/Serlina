from django.conf.urls import url
from .views import CreateUserView


urlpatterns = [
    url(r'^registeration/$', CreateUserView.as_view())
]
