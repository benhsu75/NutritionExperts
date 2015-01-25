from django.db import models
from django.contrib.auth.models import User

class Email_Signup(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	email = models.CharField(max_length=100)

class Expert_Interest_Signup(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	experience_text = models.TextField();
	other_text = models.TextField();

class Expert_Profile(models.Model):
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	title = models.CharField(max_length=100, null=True)
	organization = models.CharField(max_length=100, null=True)
	bio = models.TextField(null=True)
	website = models.URLField(null=True)
	image_path = models.CharField(max_length=100, null=True, default="gray_circle.jpg")
	is_superuser = models.BooleanField(default=True)

class Area_Of_Expertise(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)

class Accreditation(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)

class Expert_Profile_Expertise_Rel(models.Model):
	expert_profile = models.ForeignKey(Expert_Profile)
	area_of_expertise = models.ForeignKey(Area_Of_Expertise)

class Expert_Profile_Accreditation_Rel(models.Model):
	expert_profile = models.ForeignKey(Expert_Profile)
	accreditation = models.ForeignKey(Accreditation)


class Sign_Up_Code(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	code = models.CharField(max_length=100)
	is_expert = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)


class Member_Profile(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	five_words = models.CharField(max_length=200, null=True)
	bio = models.TextField(null=True)
	image_path = models.CharField(max_length=100, null=True, default="gray_circle.jpg")
	is_superuser = models.BooleanField(default=False)

class User_Profile(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, unique=True)
	is_expert = models.BooleanField(default=False)
	profile_completed = models.BooleanField(default=False)
	expert_profile = models.ForeignKey(Expert_Profile, unique=True, null=True)
	member_profile = models.ForeignKey(Member_Profile, unique=True, null=True)

# Question

class Question(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	asked_by_user = models.ForeignKey(User_Profile)

	text = models.CharField(max_length=500)
	details = models.TextField()
	num_votes = models.SmallIntegerField(null=True)
	is_active = models.BooleanField(default=False)

class Upvote_Rel(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	user_profile = models.ForeignKey(User_Profile)
	question = models.ForeignKey(Question)

class Answer(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	last_updated = models.DateTimeField(auto_now=True)
	question = models.ForeignKey(Question)
	answered_by_user = models.ForeignKey(User_Profile)
	text = models.TextField()

class Star_Rel(models.Model):
	timestamp = models.DateTimeField(auto_now_add=True)
	user_profile = models.ForeignKey(User_Profile)
	answer = models.ForeignKey(Answer)






