from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
import json
from mainapp.models import *
from django.contrib.auth import authenticate, login, logout
import time
import calendar

############################################################
#################     HELPER METHODS       #################
############################################################

# Set's up context with preliminary variables (profile picture, expert, etc)
def prepare_context(request):
	context = RequestContext(request, {})

	if request.user.is_authenticated():
		try:
			profile = User_Profile.objects.get(user=request.user)
		except User_Profile.DoesNotExist:
			logout(request)
			return context

		context['my_is_expert_flag'] = profile.is_expert
		context['my_user_profile_pk'] = profile.pk
		context['first_name'] = request.user.first_name

		# Pass User Profile object
		context['my_user_profile'] = profile

		profile_picture_loc = None
		if profile.is_expert:
			profile_picture_loc = profile.expert_profile.image_path
			context['my_is_superuser'] = False
		else:
			profile_picture_loc = profile.member_profile.image_path

			# Check if superuser
			if profile.member_profile.is_superuser:
				context['my_is_superuser'] = True
			else:
				context['my_is_superuser'] = False

		context['my_profile_picture'] = profile_picture_loc
	return context



############################################################
#################   CONTROLLER METHODS     #################
############################################################

# LANDING
# Also handles email signup form submit
def landing(request):

	if request.user.is_authenticated():
		return HttpResponseRedirect('/feed/')

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
	# Get all expert profiles and package into JSON
	expert_profiles_dict = {}

	expert_profiles = Expert_Profile.objects.all()
	for expert in expert_profiles:
		expert_profile_object = {}
		expert_profile_object['first_name'] = expert.first_name
		expert_profile_object['last_name'] = expert.last_name
		expert_profile_object['title'] = expert.title
		expert_profile_object['organization'] = expert.organization
		expert_profile_object['bio'] = expert.bio
		expert_profile_object['website'] = expert.website
		expert_profile_object['image_path'] = expert.image_path

		# Get accreditations
		accreditations_array = []
		accreditations_rels = Expert_Profile_Accreditation_Rel.objects.filter(expert_profile=expert)
		for a in accreditations_rels:
			accreditations_array.append(a.accreditation.name)
		expert_profile_object['accreditations'] = accreditations_array

		# Get expertise
		expertise_array = []
		expertise_rels = Expert_Profile_Expertise_Rel.objects.filter(expert_profile=expert)
		for e in expertise_rels:
			expertise_array.append(e.area_of_expertise.name)
		expert_profile_object['expertise'] = expertise_array

		expert_profiles_dict[expert.pk] = expert_profile_object

	template = loader.get_template('mainapp/about/experts.html')
	context = RequestContext(request, {
		'experts_data': json.dumps(expert_profiles_dict)
	})
	return HttpResponse(template.render(context))

def faq(request):
	template = loader.get_template('mainapp/about/faq.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def expert_contact(request):
	template = loader.get_template('mainapp/about/expert_contact.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def terms(request):
	template = loader.get_template('mainapp/about/terms.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

def privacy(request):
	template = loader.get_template('mainapp/about/privacy.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

def disclaimer(request):
	template = loader.get_template('mainapp/about/disclaimer.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

# APP PAGES
def sign_in(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/feed/")
	template = loader.get_template('mainapp/app/sign_in.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def feed(request):
	template = loader.get_template('mainapp/app/feed.html')
	context = prepare_context(request)

	feed_items = []

	for q in Question.objects.order_by('timestamp'):
		item = {}
		item['pk'] = q.pk 
		item['text'] = q.text
		item['num_upvotes'] = len(Upvote_Rel.objects.filter(question=q))
		feed_items.append(item)

	context['feed_items'] = json.dumps(feed_items)

	return HttpResponse(template.render(context))
	
def sign_up(request):
	template = loader.get_template('mainapp/app/sign_up.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def sign_up_profile(request):
	# If not logged in, redirect to login page
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/sign_in/")

	# Prepare template
	template = loader.get_template('mainapp/app/sign_up_profile.html')
	context = prepare_context(request)

	try:
		user_profile = User_Profile.objects.get(user=request.user)

		if user_profile.profile_completed:
			return HttpResponseRedirect("/feed/")
	except User_Profile.DoesNotExist:
		user_profile = User_Profile(user=request.user)
		user_profile.save()
	
	return HttpResponse(template.render(context))

def profile(request, user_profile_pk):
	template = loader.get_template('mainapp/app/profile.html')
	context = prepare_context(request)

	context['user_profile_pk'] = user_profile_pk

	# Check that user with pk exists, and get it
	try:
		shown_user_profile = User_Profile.objects.get(pk=user_profile_pk)
		context['profile_exists'] = True
	except User_Profile.DoesNotExist:
		context['profile_exists'] = False
		return HttpResponse(template.render(context))

	shown_is_expert = shown_user_profile.is_expert
	context['shown_is_expert'] = shown_is_expert

	# Get all information and put into context
	context['shown_first_name'] = shown_user_profile.user.first_name
	context['shown_last_name'] = shown_user_profile.user.last_name

	if shown_is_expert:
		context['shown_title'] = json.dumps(shown_user_profile.expert_profile.title)
		context['shown_organization'] = json.dumps(shown_user_profile.expert_profile.organization)
		context['shown_bio'] = json.dumps(shown_user_profile.expert_profile.bio)
		context['shown_website'] = json.dumps(shown_user_profile.expert_profile.website)
		context['shown_image_path'] = shown_user_profile.expert_profile.image_path

		# Get accreditations, package into array
		accreditations_array = []
		accreditation_rels = Expert_Profile_Accreditation_Rel.objects.filter(expert_profile=shown_user_profile.expert_profile)
		for a_rel in accreditation_rels:
			accreditations_array.append(a_rel.accreditation.name)
		context['shown_accreditations'] = json.dumps(accreditations_array)

		# Get areas of expertise, package into array
		expertise_array = []
		expertise_rels = Expert_Profile_Expertise_Rel.objects.filter(expert_profile=shown_user_profile.expert_profile)
		for e_rel in expertise_rels:
			expertise_array.append(e_rel.area_of_expertise.name)
		context['shown_expertise'] = json.dumps(expertise_array)
		
	else:
		context['shown_five_words'] = json.dumps(shown_user_profile.member_profile.five_words)
		context['shown_image_path'] = shown_user_profile.member_profile.image_path
		context['shown_bio'] = json.dumps(shown_user_profile.member_profile.bio)

	return HttpResponse(template.render(context))

def discussion(request, pk):
	template = loader.get_template('mainapp/app/discussion.html')
	context = prepare_context(request)
	
	# Get question information
	try:
		question = Question.objects.get(pk=pk)
		context['question_exists'] = True
		context['question_pk'] = pk

		# Load Question Data
		question_data = {}
		question_data['text'] = question.text
		question_data['timestamp'] = question.timestamp
		question_data['details'] = question.details
		question_data['num_votes'] = len(Upvote_Rel.objects.filter(question=question))
		context['question_data'] = question_data

		answers_array = []

		
		# Load all answers for the question
		answers = Answer.objects.filter(question=question)
		for a in answers:
			answer_object = {}
			
			answer_object['timestamp'] = calendar.timegm(a.timestamp.utctimetuple())
			answer_object['text'] = a.text
			answer_object['answered_by_user'] = a.answered_by_user

			# Get answer-by user information
			user_profile = a.answered_by_user

			answer_object['answered_by_first_name'] = user_profile.user.first_name
			answer_object['answered_by_last_name'] = user_profile.user.last_name

			answers_array.append(answer_object)

		context['answers_data'] = answers_array

	except Question.DoesNotExist:
		context['question_exists'] = False

	return HttpResponse(template.render(context))

def ask(request):
	template = loader.get_template('mainapp/app/ask.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

def answer_questions(request):
	template = loader.get_template('mainapp/app/answer_questions.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

# Expert update profile 
def expert_update(request):
	template = loader.get_template('mainapp/app/expert_update.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

# User update profile 
def user_update(request):
	template = loader.get_template('mainapp/app/user_update.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))