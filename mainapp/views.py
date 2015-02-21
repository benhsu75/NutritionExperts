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

		context['logged_in'] = True
		context['my_is_expert_flag'] = profile.is_expert
		context['my_user_profile_pk'] = profile.pk
		context['first_name'] = request.user.first_name
		context['my_last_name'] = request.user.last_name

		if profile.is_expert:
			accreditation_string = ""
			accreditation_rels = Expert_Profile_Accreditation_Rel.objects.filter(expert_profile=profile.expert_profile)
			for r in accreditation_rels:
				accreditation_string += r.accreditation.name + ", "
			go_till_index = 0
			if len(accreditation_rels) > 0:
				go_till_index = len(accreditation_string)-2
			context['my_accreditations'] = accreditation_string[:go_till_index]

		# Pass User Profile object
		context['my_user_profile'] = profile

		profile_picture_loc = None
		if profile.is_expert:
			profile_picture_loc = profile.expert_profile.image_path
			context['my_is_superuser'] = True
		else:
			profile_picture_loc = profile.member_profile.image_path

			# Check if superuser
			if profile.member_profile.is_superuser:
				context['my_is_superuser'] = True
			else:
				context['my_is_superuser'] = False

		context['my_profile_picture'] = profile_picture_loc
	else:
		context['logged_in'] = False
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

		user_profile = User_Profile.objects.get(expert_profile=expert)
		expert_profiles_dict[user_profile.pk] = expert_profile_object

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

def feed(request, state=0, current_page=0):
	template = loader.get_template('mainapp/app/feed.html')
	context = prepare_context(request)

	feed_items = []

	# Paginate
	if int(state) == 0:
		page = Question.popularity_sorted.all()
	else:
		page = Question.recent_sorted.all()

	current_page = int(current_page)
	start_index = current_page * 12
	end_index = (current_page + 1) * 12
	if end_index > len(page):
		context['next_exists'] = False
		end_index = len(page)
	elif end_index == len(page):
		context['next_exists'] = False
	else:
		context['next_exists'] = True

	page = page[start_index:end_index]

	if len(page) == 0 and current_page != 0:
		return HttpResponseRedirect('/feed/');

	for q in page:
		item = {}
		# General info
		item['pk'] = q.pk 
		item['text'] = q.text
		item['num_upvotes'] = len(Upvote_Rel.objects.filter(question=q))

		# Get pictures of experts who answered
		experts_array = []
		answers = Answer.objects.filter(question=q)
		for a in answers:
			expert_object = {}
			expert = a.answered_by_user.expert_profile # Expert_Profile
			expert_object['expert_profile_pk'] = expert.pk
			expert_object['image_path'] = expert.image_path
			experts_array.append(expert_object)
		item['experts_array'] = experts_array 

		# Upvoted
		if request.user.is_authenticated():
			user = User_Profile.objects.get(user=request.user)
			item['upvoted'] = Upvote_Rel.objects.filter(user_profile=user,question=q).count()
		feed_items.append(item)

	# Pagination values
	context['current_page'] = current_page
	context['page_number'] = current_page + 1
	context['back_page'] = current_page-1
	context['next_page'] = 1
	if current_page == 0:
		context['back_exists'] = False
	else:
		context['back_exists'] = True
	context['state'] = state
	
	context['feed_items'] = json.dumps(feed_items)

	return HttpResponse(template.render(context))
	
def sign_up(request):
	template = loader.get_template('mainapp/app/sign_up.html')
	context = prepare_context(request)

	if request.user.is_authenticated():
		return HttpResponseRedirect("/feed/")

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
		context['shown_num_answers'] = len(Answer.objects.filter(answered_by_user=shown_user_profile))

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
		context['shown_num_questions'] = len(Question.objects.filter(asked_by_user=shown_user_profile))

	feed_items = []

	questions_to_store = []

	if shown_is_expert:
		answers = Answer.objects.filter(answered_by_user=shown_user_profile)
		for a in answers:
			if a.question not in questions_to_store:
				questions_to_store.append(a.question)
	else:
		questions_to_store = Question.objects.filter(asked_by_user=shown_user_profile).order_by('-timestamp')
	
	for q in questions_to_store:
		item = {}
		# General info
		item['pk'] = q.pk 
		item['text'] = q.text
		item['num_upvotes'] = len(Upvote_Rel.objects.filter(question=q))

		# Get pictures of experts who answered
		experts_array = []
		answers = Answer.objects.filter(question=q)
		for a in answers:
			expert_object = {}
			expert = a.answered_by_user.expert_profile # Expert_Profile
			expert_object['expert_profile_pk'] = expert.pk
			expert_object['image_path'] = expert.image_path
			experts_array.append(expert_object)
		item['experts_array'] = experts_array 

		# Upvoted
		if request.user.is_authenticated():
			user = User_Profile.objects.get(user=request.user)
			item['upvoted'] = Upvote_Rel.objects.filter(user_profile=user,question=q).count()
		feed_items.append(item)
	
	context['feed_items'] = json.dumps(feed_items)

	return HttpResponse(template.render(context))

def discussion(request, pk):
	template = loader.get_template('mainapp/app/discussion.html')
	context = prepare_context(request)
	
	# Get question information
	try:
		question = Question.objects.get(pk=pk)
		context['question'] = question
		context['question_exists'] = True

		# Load Question Data
		question_data = {}
		question_data['num_votes'] = len(Upvote_Rel.objects.filter(question=question))
		context['question_data'] = question_data

		answers_array = []

		
		# Load all answers for the question
		answers = sorted(Answer.objects.filter(question=question), key=lambda n: -n.stars)
		for a in answers:
			answer_object = {}

			answer_object['object'] = a

			answer_expert_profile = a.answered_by_user.expert_profile

			accreditation_string = ""
			accreditation_rels = Expert_Profile_Accreditation_Rel.objects.filter(expert_profile=answer_expert_profile)
			for r in accreditation_rels:
				accreditation_string += r.accreditation.name + ", "
			go_till_index = 0
			if len(accreditation_rels) > 0:
				go_till_index = len(accreditation_string)-2

			answer_object['accreditation'] = accreditation_string[:go_till_index]

			comments_array = []
			comments = Comment.objects.filter(answer=a)
			for comment in comments:
				comment_object = {}
				comment_object['object'] = comment
				if comment.commented_by_user.is_expert:
					comment_object['image_path'] = comment.commented_by_user.expert_profile.image_path
					
				else:
					comment_object['image_path'] = comment.commented_by_user.member_profile.image_path

				comment_object['first_name'] = comment.commented_by_user.user.first_name
				comment_object['last_name'] = comment.commented_by_user.user.last_name
				comment_object['commenter_pk'] = comment.commented_by_user.pk

				comments_array.append(comment_object)
			answer_object['comments'] = comments_array

			answer_object['stars'] = len(Star_Rel.objects.filter(answer=a))

			# Check if user already starred
			if request.user.is_authenticated():
				user_profile = User_Profile.objects.get(user=request.user)
				try:
					s = Star_Rel.objects.get(user_profile=user_profile,answer=a)
					answer_object['already_starred'] = True
				except Star_Rel.DoesNotExist:
					answer_object['already_starred'] = False

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
	
	if request.user.is_authenticated():
		# Get all user data to send through context
		user_profile = User_Profile.objects.get(user=request.user)
		expert_profile = user_profile.expert_profile

		if expert_profile.title:
			context['title'] = expert_profile.title
		else:
			context['title'] = json.dumps("")

		if expert_profile.organization:
			context['organization'] = expert_profile.organization
		else:
			context['organization'] = json.dumps("")

		if expert_profile.bio:
			context['bio'] = expert_profile.bio
		else:
			context['bio'] = json.dumps("")

		if expert_profile.website:
			context['website'] = expert_profile.website
		else:
			context['website'] = json.dumps("")

		# Get accreditations
		accreditation_string = ""
		accreditation_rels = Expert_Profile_Accreditation_Rel.objects.filter(expert_profile=expert_profile)
		for r in accreditation_rels:
			accreditation_string += r.accreditation.name + ", "
		go_till_index = 0
		if len(accreditation_rels) > 0:
			go_till_index = len(accreditation_string)-2
		context['accreditations'] = accreditation_string[:go_till_index]

		# Get areas of expertise
		expertise_string = ""
		expertise_rels = Expert_Profile_Expertise_Rel.objects.filter(expert_profile=expert_profile)
		for r in expertise_rels:
			expertise_string += r.area_of_expertise.name + ", "
		go_till_index = 0
		if len(expertise_rels) > 0:
			go_till_index = len(expertise_string)-2
		context['expertise'] = expertise_string[:go_till_index]

		context['account_image_path'] = json.dumps(expert_profile.image_path)


		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect('/feed/')

def my_account(request):
	if request.user.is_authenticated():
		if User_Profile.objects.get(user=request.user).is_expert:
			return HttpResponseRedirect('/expert_update/')
		else:
			return HttpResponseRedirect('/user_update/')	
	else:
		return HttpResponseRedirect('/sign_in/')		

def update_password(request):
	template = loader.get_template('mainapp/app/update_password.html')
	context = prepare_context(request)
	return HttpResponse(template.render(context))

# User update profile 
def user_update(request):
	template = loader.get_template('mainapp/app/user_update.html')
	context = prepare_context(request)

	if request.user.is_authenticated():
		# Get all user data to send through context
		user_profile = User_Profile.objects.get(user=request.user)
		member_profile = user_profile.member_profile

		if member_profile.five_words:
			context['five_words'] = member_profile.five_words
		else:
			context['five_words'] = ""

		if member_profile.bio:
			context['bio'] = member_profile.bio
		else:
			context['bio'] = ""

		context['account_image_path'] = json.dumps(member_profile.image_path)


		return HttpResponse(template.render(context))
	else:
		return HttpResponseRedirect('/feed/')









