from django.urls import path, include
from .views import (PostListView)


app_name = 'insta'
urlpatters = [
    path('', PostListView.as_view(), name='post_list'),
]
