from django.urls import path
from . import views

urlpatterns = [
    path("post/", views.list_posts, name="list_posts"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path("post/new/", views.create_post, name="create_post"),
    path("post/<int:id>/edit/", views.edit_post, name="edit_post"),
    path("post/<int:id>/delete/", views.delete_post, name="delete_post"),
    path("post/<int:id>/like/", views.toggle_like, name="toggle_like"),
]
