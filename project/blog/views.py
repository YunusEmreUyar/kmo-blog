from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def homeView(request):
	context = {}
	posts = Post.objects.all()
	context["posts"] = posts
	print(context)
	return render(request, "homepage.html", context)


def ownerView(request):
	return HttpResponse("Owner View")