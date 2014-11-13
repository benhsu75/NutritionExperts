from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from mainapp.models import *

# LANDING
# Also handles email signup form submit
def landing(request):
	context = RequestContext(request, {
	})
	template = loader.get_template('mainapp/about/landing.html')
	return HttpResponse(template.render(context))

# ABOUT (5 PAGES)
def about(request):
	template = loader.get_template('mainapp/about/about.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def mission(request):
	template = loader.get_template('mainapp/about/mission.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def mission2(request):
	template = loader.get_template('mainapp/about/mission2.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def experts(request):
	template = loader.get_template('mainapp/about/experts.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def faq(request):
	template = loader.get_template('mainapp/about/faq.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def expert_contact(request, from_page):
	template = loader.get_template('mainapp/about/expert_contact.html')
	context = RequestContext(request, {
		'from_page': from_page
	})
	return HttpResponse(template.render(context))

# APP PAGES
def feed(request):
	template = loader.get_template('mainapp/app/feed.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))
	
def signup_form(request):
	template = loader.get_template('mainapp/app/signup_form.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def expert_profile(request):
	template = loader.get_template('mainapp/app/expert_profile.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def user_profile(request):
	template = loader.get_template('mainapp/app/user_profile.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def discussion(request):
	template = loader.get_template('mainapp/app/discussion.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def answer_questions(request):
	template = loader.get_template('mainapp/app/answer_questions.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

# Expert update profile 
def expert_update(request):
	template = loader.get_template('mainapp/app/expert_update.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

# User update profile 
def user_update(request):
	template = loader.get_template('mainapp/app/user_update.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))