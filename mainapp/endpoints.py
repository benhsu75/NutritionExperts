from django.http import HttpResponse, HttpResponseRedirect
import json
from mainapp.models import *
from mainapp.forms import *
from django.core.validators import validate_email # Django's Email Validator
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import random

# Error codes
# 0 - Not a valid email
# 1 - Email already signed up
def email_signup(request):
	email = request.POST.get('email', None)

	# Construct return_object
	return_object = {}

	try:
		# Validate email format
		validate_email(email)

		# Check duplicate
		num_matching_objects = Email_Signup.objects.filter(email=email).count()

		if num_matching_objects == 0:
			new_email_signup = Email_Signup(email=email, timestamp=datetime.now())
			new_email_signup.save();
			return_object['status'] = 1
		else:
			return_object['status'] = 0
			return_object['error'] = 1
	except ValidationError:
		return_object['status'] = 0
		return_object['error'] = 0
	
	return HttpResponse(json.dumps(return_object))

def expert_interest_signup(request):
	first_name = request.POST.get('first_name', None)
	last_name = request.POST.get('last_name', None)
	email = request.POST.get('email', None)
	experience_text = request.POST.get('experience_text', None)
	other_text = request.POST.get('other_text', None)

	# Construct return_object
	return_object = {}

	try:
		expert = Expert_Interest_Signup(first_name=first_name, last_name=last_name, email=email, experience_text=experience_text, other_text=other_text)
		expert.save()

		return_object['status'] = 1
	except ValidationError:
		return_object['status'] = 0
		return_object['error'] = 0

	return HttpResponse(json.dumps(return_object))

# Sign's up a new user
def sign_up_user(request):
	first_name = request.POST.get('first_name', None)
	last_name = request.POST.get('last_name', None)
	email = request.POST.get('email', None)
	password = request.POST.get('password', None)
	code = request.POST.get('code', None)

	# Validate the code
	return_object = {}
	is_expert_flag = False
	is_superuser_flag = False


	try: 
		validate_email(email)
	except ValidationError:
		return_object['status'] = 0
		return_object['error'] = 2
		return HttpResponse(json.dumps(return_object))

	try:
		validate_code = Sign_Up_Code.objects.get(code=code)
		is_expert_flag = validate_code.is_expert
		is_superuser_flag = validate_code.is_superuser
	except Sign_Up_Code.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 0
		return HttpResponse(json.dumps(return_object))

	# Validate that user with existing email doesn't exist
	existing_user = User.objects.filter(email=email)
	if existing_user.count() > 0:
		return_object['status'] = 0
		return_object['error'] = 1
		return HttpResponse(json.dumps(return_object))

	# Create new user
	new_user = User.objects.create_user(email, email, password, first_name=first_name, last_name=last_name)
	new_user.save()

	return_object['status'] = 1

	# Check for expert
	if is_expert_flag:
		return_object['is_expert_flag'] = 1
		expert_profile = Expert_Profile()
		expert_profile.save()
		profile = User_Profile(user=new_user, is_expert=True, expert_profile=expert_profile)
		profile.save()
	else:
		return_object['is_expert_flag'] = 0
		member_profile = None

		# Delegate superuser privileges to those with code
		if is_superuser_flag:
			member_profile = Member_Profile(is_superuser=True)
		else:
			member_profile = Member_Profile()

		member_profile.save()
		profile = User_Profile(user=new_user, is_expert=False, member_profile=member_profile)
		profile.save()

	# Log user in
	user = authenticate(username=email, password=password)
	if user is not None:
		login(request, user)
	
	return HttpResponse(json.dumps(return_object))

def authenticate_signin(request):
	email = request.POST.get('email', None)
	password = request.POST.get('password', None)

	return_object = {}

	user = authenticate(username=email, password=password)
	if user is not None:
		login(request, user)
		return_object['status'] = 1
	else:
		return_object['status'] = 0

	return HttpResponse(json.dumps(return_object))

def log_out(request):
	logout(request)

	return_object = {}
	return_object['status'] = 1

	return HttpResponse(json.dumps(return_object))

def populate_member_profile(request):

	return_object = {}

	# Validate that user is member
	profile = User_Profile.objects.get(user=request.user)
	if profile.is_expert:
		return_object['status'] = 0
		return HttpResponse(json.dumps(return_object))

	five_words = json.loads(request.POST.get('five_words', None))
	bio = json.loads(request.POST.get('bio', None))

	member_profile = profile.member_profile

	if member_profile == None:
		member_profile = Member_Profile()
	
	if five_words:
		member_profile.five_words = five_words
	if bio:
		member_profile.bio = bio

	member_profile.save()

	profile.profile_completed = True
	profile.save()

	return_object['status'] = 1

	return HttpResponse(json.dumps(return_object))

def post_question(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	title = json.loads(request.POST.get('title', None))
	details = json.loads(request.POST.get('details', None))

	# Validate title
	title_num_char = len(title)

	if title_num_char > 190:
		return_object['status'] = 0
		return_object['error'] = 1 # Title too long

	user_profile = User_Profile.objects.get(user=request.user)
	is_superuser = False

	if user_profile.is_expert:
		is_superuser = user_profile.expert_profile.is_superuser
	else:
		is_superuser = user_profile.member_profile.is_superuser

	# Create question
	q = Question(asked_by_user=user_profile, text=title, details=details, num_votes=0)
	q.save()

	if is_superuser: # Question is posted
		q.is_active = True
		q.save()

	return_object['status'] = 1
	return HttpResponse(json.dumps(return_object))

def answer_question(request):
	return_object = {}

	question_pk = request.POST.get('question_pk', None)
	answer_text = request.POST.get('answer_text', None)

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	# Validate that user is an expert
	user_profile = User_Profile.objects.get(user=request.user)
	if not user_profile.is_expert:
		return_object['status'] = 0
		return_object['error'] = 1 # Not an expert
		return HttpResponse(json.dumps(return_object))

	# Get question
	try:
		question = Question.objects.get(pk=question_pk)
	except Question.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Nonexistent question
		return HttpResponse(json.dumps(return_object))

	# Validate that answer isn't an empty string
	if answer_text:
		answer_text = answer_text.strip()

	if not answer_text:
		return_object['status'] = 0
		return_object['error'] = 3 # Empty string posted as answer
		return HttpResponse(json.dumps(return_object))

	# Create answer and relate to question
	a = Answer(question=question, answered_by_user=user_profile, text=answer_text)
	a.save()

	return_object['status'] = 1 # Success
	return HttpResponse(json.dumps(return_object))


def populate_expert_profile(request):
	return_object = {}

	# Validate that user is member
	profile = User_Profile.objects.get(user=request.user)
	if not profile.is_expert:
		return_object['status'] = 0
		return HttpResponse(json.dumps(return_object))

	accreditations = json.loads(request.POST.get('accreditations', None))
	title = json.loads(request.POST.get('title', None))
	organization = json.loads(request.POST.get('organization', None))
	url = json.loads(request.POST.get('url', None))
	bio = json.loads(request.POST.get('bio', None))
	areas_of_expertise = json.loads(request.POST.get('areas_of_expertise', None))

	profile = User_Profile.objects.get(user=request.user)

	expert_profile = profile.expert_profile

	if expert_profile == None:
		expert_profile = Expert_Profile()
	
	if title:
		expert_profile.title = title
	if organization:
		expert_profile.organization = organization
	if url:
		expert_profile.website = url
	if bio:
		expert_profile.bio = bio

	expert_profile.first_name = request.user.first_name
	expert_profile.last_name = request.user.last_name

	expert_profile.save()

	profile.expert_profile = expert_profile
	

	# Handle Accreditations
	for s in accreditations:
		a = None
		try:
			a = Accreditation.objects.get(name=s)
		except Accreditation.DoesNotExist:
			a = Accreditation(name=s)
			a.save()
		rel = Expert_Profile_Accreditation_Rel(expert_profile=expert_profile, accreditation=a)
		rel.save()

	# Handle areas of expertise
	for s in areas_of_expertise:
		e = None
		try:
			e = Area_Of_Expertise.objects.get(name=s)
		except Area_Of_Expertise.DoesNotExist:
			e = Area_Of_Expertise(name=s)
			e.save()
		rel = Expert_Profile_Expertise_Rel(expert_profile=expert_profile, area_of_expertise=e)
		rel.save()

	profile.profile_completed = True
	profile.save()
	expert_profile.save()

	return_object['status'] = 1

	return HttpResponse(json.dumps(return_object))

def upvote_question(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	question_pk = request.POST.get('question_pk', None)

	try:
		user = User_Profile.objects.get(user=request.user)
		question = Question.objects.get(pk=question_pk)

		already_upvoted = Upvote_Rel.objects.get(user_profile=user,question=question)

		# User already upvoted
		return_object['status'] = 0
		return_object['error'] = 3 # User already upvoted
		return HttpResponse(json.dumps(return_object))

	# Validate that user exists
	except User_Profile.DoesNotExist: 
		return_object['status'] = 0
		return_object['error'] = 1 # User doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that question exists
	except Question.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Question doesn't exist
		return HttpResponse(json.dumps(return_object))
	except Upvote_Rel.DoesNotExist:
		# Create new Upvote_Rel
		u = Upvote_Rel(user_profile=user, question=question)
		u.save()

		# Return
		return_object['status'] = 1
		return_object['num_votes'] = Upvote_Rel.objects.filter(question=question).count()
		return HttpResponse(json.dumps(return_object))

def remove_upvote_question(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	question_pk = request.POST.get('question_pk', None)

	try:
		user = User_Profile.objects.get(user=request.user)
		question = Question.objects.get(pk=question_pk)

		already_upvoted = Upvote_Rel.objects.get(user_profile=user,question=question)
		already_upvoted.delete();

		# Return
		return_object['status'] = 1
		return_object['num_votes'] = Upvote_Rel.objects.filter(question=question).count()
		return HttpResponse(json.dumps(return_object))

	# Validate that user exists
	except User_Profile.DoesNotExist: 
		return_object['status'] = 0
		return_object['error'] = 1 # User doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that question exists
	except Question.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Question doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that question has been upvoted by user
	except Upvote_Rel.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 3
		return HttpResponse(json.dumps(return_object))



def star_answer(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	user_pk = request.POST.get('user_pk', None)
	answer_pk = request.POST.get('answer_pk', None)

	try:
		user = User_Profile.objects.get(pk=user_pk)

		answer = Answer.objects.get(pk=answer_pk)

		already_starred = Star_Rel.objects.get(user_profile=user, answer=answer)

		# User already starred
		return_object['status'] = 0
		return_object['error'] = 3 # User already starred
		return HttpResponse(json.dumps(return_object))
	# Validate that user exists
	except User_Profile.DoesNotExist: 
		return_object['status'] = 0
		return_object['error'] = 1 # User doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that question exists
	except Question.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Question doesn't exist
		return HttpResponse(json.dumps(return_object))
	except Star_Rel.DoesNotExist:
		# Create new Star_Rel
		s = Star_Rel(user_profile=user, answer=answer)
		s.save()

		# Return
		return_object['status'] = 1

		answer = Answer.objects.get(pk=answer_pk)
		return_object['num_stars'] = Star_Rel.objects.filter(answer=answer).count()
		return HttpResponse(json.dumps(return_object))

def unstar_answer(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	user_pk = request.POST.get('user_pk', None)
	answer_pk = request.POST.get('answer_pk', None)

	try:
		user = User_Profile.objects.get(pk=user_pk)

		answer = Answer.objects.get(pk=answer_pk)

		already_starred = Star_Rel.objects.get(user_profile=user, answer=answer)
		already_starred.delete()

		# Return
		return_object['num_stars'] = Star_Rel.objects.filter(answer=answer).count()
		return_object['status'] = 1
		return HttpResponse(json.dumps(return_object))
	# Validate that user exists
	except User_Profile.DoesNotExist: 
		return_object['status'] = 0
		return_object['error'] = 1 # User doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that question exists
	except Question.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Question doesn't exist
		return HttpResponse(json.dumps(return_object))
	except Star_Rel.DoesNotExist:
		# User already starred
		return_object['status'] = 0
		return_object['error'] = 3 # User never starred
		return HttpResponse(json.dumps(return_object))
		
def comment(request):
	return_object = {}

	# Validate logged in
	if not request.user.is_authenticated():
		return_object['status'] = 0
		return_object['error'] = 0 # Not logged in
		return HttpResponse(json.dumps(return_object))

	answer_pk = request.POST.get('answer_pk', None)
	text = request.POST.get('text', None)

	try:
		user = User_Profile.objects.get(user=request.user)

		answer = Answer.objects.get(pk=answer_pk)

		comment = Comment(answer=answer, commented_by_user=user, text=text)
		comment.save()

		# Return
		return_object['status'] = 1
		return_object['comment_text'] = text
		if user.is_expert:
			return_object['file_path'] = user.expert_profile.image_path
		else:
			return_object['file_path'] = user.member_profile.image_path
		return_object['first_name'] = user.user.first_name
		return_object['last_name'] = user.user.last_name
		return HttpResponse(json.dumps(return_object))
	# Validate that user exists
	except User_Profile.DoesNotExist: 
		return_object['status'] = 0
		return_object['error'] = 1 # User doesn't exist
		return HttpResponse(json.dumps(return_object))
	# Validate that answer exists
	except Answer.DoesNotExist:
		return_object['status'] = 0
		return_object['error'] = 2 # Answer doesn't exist
		return HttpResponse(json.dumps(return_object))

def upload_profile_picture(request):
	return_object = {}

	if request.method == 'POST':
		form = PhotoUploadForm(data=request.POST, files=request.FILES)
		u = request.user
		profile = User_Profile.objects.get(user=u)
		

		# Create filename and move file
		r = random.randrange(0,1000000)
		new_filename = str(r)+'_'+request.FILES['photo'].name
		new_filepath = 'mainapp/static/mainapp/images/profile_pictures/' + new_filename
		handle_uploaded_file(request.FILES['photo'], new_filepath)

		# Update profile picture path in db

		if profile.is_expert:
			expert_profile = profile.expert_profile
			if expert_profile == None:
				expert_profile = Expert_Profile(image_path=new_filename)
			else:
				expert_profile.image_path = new_filename
			expert_profile.save()
		else:
			member_profile = profile.member_profile
			if member_profile == None:
				member_profile = Member_Profile(image_path=new_filename)
			else:
				member_profile.image_path = new_filename
			member_profile.save()
		
	return_object['status'] = 1
	return_object['profile_picture_filename'] = new_filename

	return HttpResponse(json.dumps(return_object))

def get_feed_items(request):
	return_object = {}

	state = int(request.POST.get('state', None))

	feed_items = []

	# 0 = popularity, 1 = recent
	if state == 0: # Popularity
		feed_items = []
		
	else: # Recent
		for q in Question.objects.order_by('timestamp'):
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

	return_object['feed_items'] = json.dumps(feed_items)
	return_object['status'] = 1
	return_object['state'] = state

	return HttpResponse(json.dumps(return_object))


# Helper method for uploading photo
def handle_uploaded_file(f, new_filepath):
    with open(new_filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)





