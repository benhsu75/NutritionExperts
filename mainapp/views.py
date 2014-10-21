from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

# About page
def about(request):
	template = loader.get_template('mainapp/about.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

# Landing page
def landing(request):
	template = loader.get_template('mainapp/landing.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

# Sign up page
def signup(request):
	template = loader.get_template('mainapp/signup.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))