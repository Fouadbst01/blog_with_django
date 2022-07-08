from anyio import get_all_backends
from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from myblog.models import Blog
from .forms import RegisterForm,SaveBlgoForm
from django.contrib.auth import login,logout,authenticate


def home_view(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.filter(auteur=request.user.id)
        if not blogs:
            blogs=[]
    else:
        blogs = get_list_or_404(Blog)
    return render(request,'blogs.html',{
        "blogs":blogs
    })

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('myblog:home')
    else :
        form = RegisterForm()
    return render(request,'registration/sign_up.html',{"form":form})

def delete_blog(request,id_blog):
    blog= get_object_or_404(Blog,pk=id_blog)
    blog.delete()
    return redirect('myblog:home')

def new_blog(request):
    if request.method == 'POST':
        form = SaveBlgoForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False) 
            # for test propose
            # add blog to user
            blog.auteur = request.user
            blog.save()
            return redirect('myblog:home')
    else :
        form = SaveBlgoForm()

    return render(request,'blog/saveForm.html',{"form":form})