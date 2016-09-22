from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify
from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {
        'posts': posts,
    })


def post_detail(request, post_name):
    post = get_object_or_404(Post, route=post_name)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def post_publish(request, post_name):
    post = get_object_or_404(Post, route=post_name)
    post.publish()
    return redirect('post_detail', post_name=post.route)


def post_remove(request, post_name):
    post = get_object_or_404(Post, route=post_name)
    post.delete()
    return redirect('post_list')


def post_new(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        # TODO: Add non unique route handler
        if form.is_valid():
            post = form.save(commit=False)
            post.route = slugify(post.title, allow_unicode=True)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_name=post.route)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })


def post_edit(request, post_name):
    post = get_object_or_404(Post, route=post_name)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_name=post.route)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
