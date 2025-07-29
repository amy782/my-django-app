from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, Profile
from .forms import Blogform, Profileform
from django.contrib import messages

def user_signup(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "YOUR ACCOUNT IS CREATED!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "YOUR ACCOUNT IS LOGGED OUT")
    return redirect('login')

@login_required
def index(request):
    return render(request,'index.html')

@login_required
def create_post(request):
    if request.method == "POST":
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit = False)
            blog.author = request.user
            blog.save()
            messages.success(request, "YOUR BLOG IS POSTED!")
            return redirect("home")
    else:
        form = Blogform()
    return render(request, 'create_post.html',{"form": form})

@login_required
def my_posts(request):
    user = request.user
    blogs = Blog.objects.filter(author = user)
    return render(request, 'my_posts.html', {"blogs": blogs})

def all_posts(request):
    blogs = Blog.objects.all()  
    return render(request,'all_posts.html',{'blogs':blogs})

@login_required
def dlt(request, pk):
    blog = get_object_or_404(Blog, id=pk)

    # Only allow the author to delete their post
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == "POST":
        blog.delete()
        messages.success(request, "YOUR BLOG IS DELETED!")
        return redirect("all_posts")

    return render(request, 'dlt.html', {"blog": blog})

@login_required
def edit(request, pk):
    blog = get_object_or_404(Blog, id = pk)
    # only allow author to edit
    if blog.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == "POST":
        form = Blogform(request.POST, request.FILES, instance= blog)
        if form.is_valid():
            form.save()
            messages.success(request, "YOUR BLOG IS UPDATED!")
            return redirect("all_posts")
    else:
        form = Blogform(instance=blog)
    return render(request,"edit.html",{"blog": blog, "form": form})
 
@login_required
def view_profile(request):
    profile = request.user.profile
    return render(request,'profile.html',{"profile": profile})

def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES, instance= profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Profileform( instance= profile)
    return render(request, 'edit_profile.html',{'form': form})