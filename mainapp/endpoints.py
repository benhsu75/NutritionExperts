from django.http import HttpResponse
import json
from mainapp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email # Django's Email Validator
from django.core.exceptions import ValidationError


# Error codes
# 0 - Not a valid email
# 1 - Email already signed up
@csrf_exempt
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
			new_email_signup = Email_Signup(email=email)
			new_email_signup.save();
			return_object['status'] = 1
		else:
			return_object['status'] = 0
			return_object['error'] = 1
	except ValidationError:
		return_object['status'] = 0
		return_object['error'] = 0
	
	return HttpResponse(json.dumps(return_object))

@csrf_exempt
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



