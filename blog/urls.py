# blog/urls.py
from django.urls import path
from . import views
# from .views import (
#     PostListView, PostDetailView, PostCreateView
# )

urlpatterns = [
    # path("", PostListView.as_view(), name="list_posts"),
    # path("post/new/", PostCreateView.as_view(), name="create_post"),
    # path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),
    path("post/", views.list_posts, name="list_posts"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/new/", views.create_post, name="create_post"),
    path("post/<int:id>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:id>/delete/", views.delete_post, name="delete_post"),
    path("post/<int:id>/like/", views.toggle_like, name="toggle_like"),
]
