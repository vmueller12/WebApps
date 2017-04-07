from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Tutorial
# Create your views here.


def post_create(request):
	return HttpResponse("<h1>Create</h1>")


def post_detail(request, id):
	#instance = Tutorial.objects.get(id=8)
	instance = get_object_or_404(Tutorial, id=id)
	template = "post_detail.html"
	context = {
		"title": instance.title,
		"instance": instance,
	}

	return render(request, template, context)


def post_list(request):
	queryset = Tutorial.objects.all()

	context = {
		"object_list": queryset,
		"title": "List"
	}

	template = "index.html"
	return render(request, template, context)


def post_update(request):
	return HttpResponse("<h1>Update</h1>")


def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")