from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Post, Hapus
from .forms import PostCreateForm, PostDeleteForm, UserLoginForm, UserRegistrationForm

User = get_user_model()
# Create your views here.

def userlogin(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid() and request.user.is_authenticated():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())
		return	HttpResponseRedirect("/list/")

	return render(request, "login.html", {"form" : form, "title" : title})
 
def user_register(request):
	print(request.user.is_authenticated())
 	title = "Registration"
 	form = UserRegistrationForm(request.POST or None)
 	if form.is_valid():
 		user = form.save(commit = False)
 		password = form.cleaned_data.get("password")
 		user.set_password(password)
 		user.save()
 		
 		new_user = authenticate(username = user.username, password = password)
 		login(request, new_user)
 		return HttpResponseRedirect("/")

 	context = {
 		"form" : form,
 		"title" : title,
 	}
 	return render(request, "register.html", context)

def post_create(request):
	form = PostCreateForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print form.cleaned_data.get("title")
		instance.save()
		return	 HttpResponseRedirect("/list/")

	context = {
		"title" : "Create",
		"form" : form
	}

	return render(request, "post_create.html", context)


def post_list(request):
	lipost = Post.objects.all()
	us = User.objects.all()
	context = {
		"lipost" : lipost,
		"title" : "List",
		"User" : us,
	}

	return render(request, "post_list.html", context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id) 
	context = {
		"instance" : instance,
		"title" : "Detail"
	}

	return render(request, "post_detail.html", context)


def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostCreateForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()

	context = {
		"title" : "Create",
		"instance" : instance,
		"form" : form
	}

	return render(request, "post_update.html", context)


def post_delete(request, id):
	instance = Post.objects.get(id = id)
	if request.method == "POST":
		form = PostDeleteForm(request.POST, instance = instance)
		if form.is_valid():
			instance.delete()
			return HttpResponseRedirect("/list/")

	return render(request, "post_delete.html", {})

def post_logout(request):
	logout(request)
	return render(request, "login.html", {})