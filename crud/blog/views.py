from django.shortcuts import render, redirect
#######################################
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import PostForm
from .models import Post
# Create your views here.

# Home & board


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm
        return render(request, 'new.html', {'form': form})


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post': post})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})


def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


# Authentification 관련 #

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'home.html')
