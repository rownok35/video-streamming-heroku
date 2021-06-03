from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from App_Login.models import UserProfile, Follow
from django.contrib.auth.models import User

from App_Posts.models import Post, Like, Dislike, Comment
from App_Posts.forms import CommentForm

# Create your views here.


@login_required
def home(request):
    # following_list = Follow.objects.filter(follower=request.user)
    # posts = Post.objects.filter(author__in=following_list.values_list('following'))
    # liked_post = Like.objects.filter(user=request.user)
    # liked_post_list = liked_post.values_list('post', flat=True)
    # print(liked_post_list)
    post_list = Post.objects.all()
    if request.method == 'GET':
        search = request.GET.get('search', '')
        result = User.objects.filter(username__icontains=search)
        result2 = Post.objects.filter(caption__icontains=search)
        result3 = Post.objects.filter(catagory__icontains=search)

    # return render(request, 'App_Posts/home.html', context={'title':'Home', 'search':search,
    #                                                        'result':result, 'posts':posts, 'liked_post_list':liked_post_list})
    return render(request, 'App_Posts/home.html', context={'title': 'Home', 'search': search, 'result': result, 'post_list': post_list, 'result2': result2, 'result3': result3})


@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_disliked = Dislike.objects.filter(post=post, user=request.user)

    if already_disliked:
        already_disliked.delete()

    if already_liked:
        already_liked.delete()

    elif not already_liked:
        liked_post = Like(post=post, user=request.user)
        liked_post.save()
    return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk': pk}))


@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_liked.delete()

    already_disliked = Dislike.objects.filter(post=post, user=request.user)

    if already_disliked:
        already_disliked.delete()
    elif not already_disliked:
        disliked_post = Dislike(post=post, user=request.user)
        disliked_post.save()

    return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk': pk}))


@login_required
def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    comment_form = CommentForm()
    already_liked = Like.objects.filter(post=post, user=request.user)
    already_disliked = Dislike.objects.filter(post=post, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if already_disliked:
        disliked = True
    else:
        disliked = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('App_Posts:post_details', kwargs={'pk': pk}))
    return render(request, 'App_Posts/post_details.html', context={'post': post, 'comment_form': comment_form, 'liked': liked, 'disliked': disliked})
