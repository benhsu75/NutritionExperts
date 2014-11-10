from django.db import models

class Email_Signup(models.Model):
	email = models.CharField(max_length=100)

class Expert_Interest_Signup(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	experience_text = models.TextField();
	other_text = models.TextField();