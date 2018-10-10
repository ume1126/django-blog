from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Comment
from . import forms

def post_list(request):
    posts = Post.objects.all()
    form = forms.SearchForm()
    print(request.GET)

    if request.GET.get('q'):
        posts = posts.filter(title__contains = request.GET.get('q')) #titleにqを含む、部分一致検索が可能

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'form': form
    })


def article(request, pk):
    article = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=article)

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            comment.author = request.user
            comment.save()
    else:
        form = forms.CommentForm()

    print(article)
    return render(request, 'blog/article.html', {
        'article': article,
        'form': form,
        'comments': comments
    })


def delete_comment(request, pk, comment_pk):
    comment = Comment.objects.get(id=comment_pk)
    post_id = pk
    if request.user.id == comment.author.id or \
       request.user.id == comment.post.author.id:
        comment.delete()
    return redirect('blog:article', pk=post_id)


def create_article(request):
    form = forms.PostForm()
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('blog:article', pk=post.id)

    return render(request, 'blog/create_article.html', {
        'form': form
    })

def edit_article(request, pk):
    article = Post.objects.get(id=pk)

    if request.user.id == article.author.id:
        if request.method == "POST":
            form = forms.PostForm(request.POST, instance=article)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
            return redirect('blog:article', pk=article.id)
        else:
            form = forms.PostForm(instance=article)
            print(form)
    else:
        return redirect('blog:article', pk=article.id)

    return render(request, 'blog/edit_article.html', {
        'article':article, 'form':form
    })

def delete_article(request, pk):
    article = Post.objects.get(id=pk)

    if request.user.id == article.author.id:
        article.delete()
    return redirect('blog:post_list')
