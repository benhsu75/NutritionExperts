from mainapp.models import *

def create_expert_accounts():

	# Create's an expert user object and expert profile
	def create_expert(dict):
		existing_user = User.objects.filter(email=info['email'])
		if len(existing_user) == 0:
			new_user = User.objects.create_user(info['email'], info['email'], info['temp_password'], first_name=info['first_name'], last_name=info['last_name'])
			new_user.save()

			expert_profile = Expert_Profile(first_name=new_user.first_name, last_name=new_user.last_name)
			if info['title']:
				expert_profile.title = info['title']
			if info['organization']:
				expert_profile.organization = info['organization']
			if info['url'] and info['url'] != "":
				expert_profile.website = info['url']
			if info['bio']:
				expert_profile.bio = info['bio']
			if info['image_path'] != "" and info['image_path'] != None:
				expert_profile.image_path = info['image_path']
			
			expert_profile.save()

			# Handle Accreditations
			accreditations = info['accreditations'].split(',')
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
			areas_of_expertise = info['areas_of_expertise'].split(',')
			for s in areas_of_expertise:
				s = s.strip()
				e = None
				try:
					e = Area_Of_Expertise.objects.get(name=s)
				except Area_Of_Expertise.DoesNotExist:
					e = Area_Of_Expertise(name=s)
					e.save()
				rel = Expert_Profile_Expertise_Rel(expert_profile=expert_profile, area_of_expertise=e)
				rel.save()
			expert_profile.save()

			# Create user profile
			user_profile = User_Profile(user=new_user, is_expert=True, profile_completed=True, expert_profile=expert_profile)
			user_profile.save()


	# Bart de Jonghe
	info = {}
	info['email'] = 'bartd@nursing.upenn.edu'
	info['first_name'] = 'Bart'
	info['last_name'] = 'de Jonghe'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'PhD'
	info['areas_of_expertise'] = 'Obesity, Energy Balance, Eating Disorders'
	info['title'] = 'Associate Professor of Nutrition'
	info['organization'] = 'University of Pennsylvania'
	info['url'] = 'http://www.nursing.upenn.edu/faculty/profile.asp?pid=2960'
	info['bio'] = 'Dr. De Jonghe is an Assistant Professor of Nursing and obesity researcher in the University of Pennsylvania\'s School of Nursing. Dr. De Jonghe teaches "Nutrition: Science and Applications" (NURS 112), the introductory course in Penn\'s Nutrition Minor program. Dr. De Jonghe\'s research focuses on the nutritional, physiological, neuronal, and cellular signaling controls of energy balance with relevance to obesity, type 2 diabetes, and chemotherapy-induced nausea and vomiting. Dr. De Jonghe received his Ph.D. in Nutritional Sciences from the Pennsylvania State University in 2006, after which he entered a two-year Postdoctoral Fellowship in Neurophysiology at the Monell Chemical Senses Center to study nausea, vomiting and malaise.'
	info['image_path'] = 'bart_de_jonghe.jpg'
	create_expert(info)

	info['email'] = 'cbmzeoli@aol.com'
	info['first_name'] = 'Mary'
	info['last_name'] = 'Zeoli'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'RD'
	info['areas_of_expertise'] = 'Chronic Diseases, General Nutrition, Nutrition through the Lifecycle'
	info['title'] = 'Registered Dietitian'
	info['organization'] = ''
	info['url'] = ''
	info['bio'] = 'Mary is a Registered Dietitan and Registered Nurse passionate about using nutrition to enhance health through the lifespan and minimize the effects of chronic disease. She does nutrition consulting in a nursing home, works a school system, and applies nutrition concepts in the context of food catering and event organization. Mary received her BS in Food and Nutrition from SUNY Plattsburgh and her MS in Nutrition and Exercise from NYU.'
	info['image_path'] = ''
	create_expert(info)

	
