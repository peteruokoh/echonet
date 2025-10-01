from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm, CommentForm
from .models import Post, Comment, Like
from datetime import datetime

def list_posts(request):
    posts = Post.objects.all().order_by("-publishDate")
    return render(request, "list_posts.html", {"posts": posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()
    is_liked = False
    if request.user.is_authenticated:
        is_liked = Like.objects.filter(post=post, user=request.user).exists()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.commentDate = datetime.today()
            comment.save()
            return redirect("post_detail", id=post.id)
    else:
        comment_form = CommentForm() # Display empty comment form

    return render(request, "post_detail.html", {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "is_liked": is_liked,
        "total_likes": post.total_likes(),
        "total_comments": post.total_comments(),
    })

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publishDate = datetime.today()
            post.save()
            return redirect("list_posts")
    else:
        form = PostForm()
    return render(request, "create_edit_post.html", {"form": form})

@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    # If user is not the author, don't allow edit
    if request.user != post.author:
        return render(request, "edit_post_error.html", {
            "post": post
        })

    # Only the author reaches here
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "create_edit_post.html", {"form": form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # If user is not the author, don't allow delete
    if request.user != post.author:
        return render(request, "delete_post_error.html", {
            "post": post
        })
    
    # Only the author reaches here
    if request.method == "POST":
        post.delete()
        return redirect("list_posts")
    return render(request, "confirm_post_delete.html", {"post": post})

@login_required
def toggle_like(request, id):
    post = get_object_or_404(Post, id=id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:  # Already liked → Unlike
        like.delete()
    return redirect("post_detail", id=post.id)