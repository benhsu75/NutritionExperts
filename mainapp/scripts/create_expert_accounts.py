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

	info['email'] = 'melissafoor@gmail.com'
	info['first_name'] = 'Melissa'
	info['last_name'] = 'Foor'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'RDN'
	info['areas_of_expertise'] = 'Food Allergies, Gluten Free, General Nutrition'
	info['title'] = 'Registered Dietitian'
	info['organization'] = ''
	info['url'] = ''
	info['bio'] = 'Melissa is a Registered Dietitian Nutrionist and completed her dietetic internship at the St. Anthony\'s Memorial Hospital. She completed her Master\'s thesis on the effect of dark chocolate on blood pressure at the Eastern Illinois University. She will begin working at OrthoIndy as a Clinical Nutrition Manager in December.'
	info['image_path'] = 'melissa_foor.jpg'
	create_expert(info)

	info['email'] = 'flaviaherzogrd@yahoo.com'
	info['first_name'] = 'Flavia'
	info['last_name'] = 'Herzog Liebel'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MA, RD, LDN'
	info['areas_of_expertise'] = 'Eating Disorders, Weight Management Pediatrics, Nutrition Therapy'
	info['title'] = 'CEO'
	info['organization'] = 'Therapeutic Nutrition'
	info['url'] = ''
	info['bio'] = 'Flavia Herzog Liebel is a Registered Dietitian with her own nutrition practice- Therapeutic Nutrition, and has over 12 years of nutrition counseling and corporate wellness experience. Flavia also works as a consultant for Wellness Concepts, Keystone Eye Associates and St. Joseph University women\'s basketball team. Some of her previous consulting work includes Next Generation Dining and Vending, Guardian Nurses, Philadelphia Maven (as a featured writer) and Zarett Rehab. In addition to the work described above, Flavia is often interviewed as a nutrition expert. She has appeared on CBS 3 NEWS, Speak Up!, CNN Comcast Newsmakers, Good Day Philadelphia, and Your Morning on CN8 and is often quoted in newspaper, magazine and internet articles.'
	info['image_path'] = 'flavia_herzog_2.jpg'
	create_expert(info)

	info['email'] = 'mvk13@psu.edu'
	info['first_name'] = 'Matam'
	info['last_name'] = 'Vijay-Kumar'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'PhD'
	info['areas_of_expertise'] = 'Nutritional Biochemistry, Inflammation'
	info['title'] = 'Professor and Researcher'
	info['organization'] = 'Pennsylvania State University'
	info['url'] = 'http://nutrition.hhd.psu.edu/directory/Bio.aspx?id=VijayKumar'
	info['bio'] = 'Dr. Vijay-Kumar is an Assistant Professor and Researcher at the Pennsylvania State University\'s Department of Nutritional Sciences. Dr. Vijay-Kumar\'s areas of interest include Host Metabolic Adaptations to Inflammation, Innate Immunity-Gut Microbiotal Interactions in Metabolic Diseases, and Iron Homeostasis in Inflammaton. He received his Ph.D. in Biochemistry at the Central Food Technological Research Institute in Mysore, India.'
	info['image_path'] = 'matam_vijay_kumar.jpg'
	create_expert(info)

	info['email'] = 'steve@stevedupont.com'
	info['first_name'] = 'Steve'
	info['last_name'] = 'Dupont'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'RD, LD'
	info['areas_of_expertise'] = 'Weight Loss, Micronutrient Deficiencies, Juicing, Diabetes'
	info['title'] = 'Clinical Dietitian'
	info['organization'] = 'University of Alabama at Birmingham (UAB) Hospital'
	info['url'] = 'http://www.stevedupont.com/'
	info['bio'] = 'A veritable journeyman and humble rider of the space-time continuum, Steve has pursued several passions during his career. After graduating from Vanderbilt University (1996) with a degree in English/Creative Writing, he enjoyed brief success as a freelance journalist and author of two books -- including Therein Lies the Problem, a novel. Then, after studying nutrition independently for several years, he returned to school and ultimately completed a dietetic internship program at UAB. He has worked as a clinical dietitian at UAB Hospital since 2012. He has also been in private practice since 2013 and started a podcast in 2014 called Cutting Through the Nutrition Nonsense. Additionally, Steve has appeared on NPR and Fox News as a nutrition spokesman. He lives in beautiful Birmingham, Alabama with his wife and two children.'
	info['image_path'] = 'steve_dupont.jpg'
	create_expert(info)

	info['email'] = 'aub47@psu.edu'
	info['first_name'] = 'Alison'
	info['last_name'] = 'Borkowska'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'PhD'
	info['areas_of_expertise'] = 'Lipid Metabolism, Weight Loss, Inter-individual Variability, Micronutrient Biochemistry'
	info['title'] = 'Instructor'
	info['organization'] = 'The Pennsylvania State University, Department of Nutritional Sciences'
	info['url'] = 'http://nutrition.hhdev.psu.edu/directory/Bio.aspx?id=AlisonBorkowska'
	info['bio'] = 'Dr. Borkowska teaches undergraduate nutrition at Penn State. She came by way of Massachusetts General Hospital, where she was working in research pertaining to HIV infection and cardiovascular disease. Prior to her appointment there, she worked at the University of Copenhagen in the Department of Biology. There she studied adipose physiology. She completed her PhD at the University of California, Davis in Nutritional Biology. Her dissertation work focused on targeted metabolomics in the context of omega-3 fatty acid supplementation.'
	info['image_path'] = 'alison_borkowska.jpg'
	create_expert(info)

	info['email'] = 'lakan002@umn.edu'
	info['first_name'] = 'Andrew'
	info['last_name'] = 'Lakanen'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MS, RDN'
	info['areas_of_expertise'] = 'Public Health, Mediterranean Diet'
	info['title'] = 'Nutritionist and Statistician'
	info['organization'] = 'St. Paul Radiology'
	info['url'] = ''
	info['bio'] = 'Andrew is a Registered Dietitian Nutritionist and Statistician at St. Paul Radiology. He\'s engaging in the MediVat Study, a 12-month clinical trial investigating the effects of the Mediterranean-style Diet on visceral fat. In addition to research, Andrew focuses on Public Health and Health Promotion.'
	info['image_path'] = 'andrew_lakanen.jpg'
	create_expert(info)

	info['email'] = 'qamaz25@email.tamu.edu'
	info['first_name'] = 'Zubaida'
	info['last_name'] = 'Qamar'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MS'
	info['areas_of_expertise'] = 'General Nutrition, Nutrition in Minorities, Community Nutrition, Weight Management'
	info['title'] = 'Doctoral Student'
	info['organization'] = 'Texas A&M University'
	info['url'] = ''
	info['bio'] = 'Zubaida is a PhD student at Texas A&M University with her dissertation focus in nutrition education programs in minority populations using web-based resources. She is passionate about preventative nutrition and using nutrition to obtain optimal health at all stages of life along with prevention of diseases. She loves to teach and enjoys her job as a teaching assistant. She received her B.S. in Dietetics with a concentration in pre-medicine from State University of New York (SUNY) at Oneonta and her M.S. in Nutritional Sciences from Texas A&M University.'
	info['image_path'] = 'zubaida_qamar.jpg'
	create_expert(info)

	info['email'] = 'goodd@vt.edu'
	info['first_name'] = 'Deborah'
	info['last_name'] = 'Good'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'PhD'
	info['areas_of_expertise'] = 'Obesity, Genetics, Vitamin and Minerals, Neuroendocrine Systems, Exercise'
	info['title'] = 'Associate Professor'
	info['organization'] = 'Virginia Tech, Department of Human Nutrition, Foods and Exercise'
	info['url'] = 'https://www.hnfe.vt.edu/People/faculty/Biographies/good.html'
	info['bio'] = 'Dr. Deborah J. Good obtained her Ph.D. in Molecular and Cellular Biology from Northwestern University in 1992, where she was awarded a patent for her work to identify a naturally-occurring inhibitor of angiogenesis, thrombospondin. In 1997, Dr. Good accepted a position for a tenure-track Assistant Professor in the Department of Veterinary and Animal Sciences at the University of Massachusetts-Amherst, where she was awarded tenure in 2003. She moved to Virginia Tech in 2006, and since starting her independent laboratory, she has secured over 1.77 million dollars in awards and published over 50 journal articles and book chapters on the genetics of body weight regulation. Her research program is recognized internationally in the area of the molecular, genetic, and neuroendocrine control of body weight. Outside of her research and work on her lab, she plays in a community band, loves animals, and cooks with her family.'
	info['image_path'] = 'deborah_good.jpg'
	create_expert(info)

	info['email'] = 'aed76@drexel.edu'
	info['first_name'] = 'Abby'
	info['last_name'] = 'Gilman'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MS, RD, LDN'
	info['areas_of_expertise'] = 'Childhood Obesity, Research, Healthy Cooking'
	info['title'] = 'Registered Dietitian, Project Manager - Healthy Futures Initiative'
	info['organization'] = 'Drexel University'
	info['url'] = ''
	info['bio'] = "Registered Dietitian, Project Manager - Healthy Futures Initiative", "Drexel University", 'Abby Gilman is the Project Manager of the Healthy Futures Initiative at Drexel University. She is also a Registered Dietitian, and has worked both in the clinical and community setting. Her most recent work was in a community hospital providing medical nutrition therapy to hospital patients. There, she stood as a representative of the hospital dietitians on a collaborative Diabetes Outreach committee. Abby received her undergraduate degree in Health & Exercise Science from Syracuse University (Syracuse, NY) and her Master\'s Degree in Human Nutrition from Drexel University (Philadelphia, PA). Abby has also been published in two different textbooks, highlighting her research in Magnesium and the Metabolic Syndrome and Childhood Obesity.'
	info['image_path'] = 'abby_gilman.jpg'
	create_expert(info)

	info['email'] = 'bcleven3@yahoo.com'
	info['first_name'] = 'Bonnie'
	info['last_name'] = 'Cleven'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'RD'
	info['areas_of_expertise'] = 'Nutritional Wellness, Weight and Disease Management'
	info['title'] = 'Registered Dietitian'
	info['organization'] = 'YMCA of Fox Cities and Indiglo Med Spa'
	info['url'] = ''
	info['bio'] = 'Bonnie Cleven is a Registered Dietitian and is currently employed by the YMCA of the Fox Cities and Indiglo Med Spa promoting nutritional health and wellness for weight and disease management. She is in process of launching her own nutritional consulting service by phone and webcam.  Previously, she has completed writing for local newspaper and online. Cleven attained her Bachelor of Science degree by majoring in Human Biology with an Emphasis in Nutritional Science at the University of Wisconsin-Green Bay and her dietetic internship at the Iowa State University.'
	info['image_path'] = 'bonnie_cleven.jpg'
	create_expert(info)

	info['email'] = 'piorio@comcast.net'
	info['first_name'] = 'Patricia M.'
	info['last_name'] = 'Iorio'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MS, RDN, LDN'
	info['areas_of_expertise'] = 'Geriatric Nutrition, Weight Management, Food Safety, Senior Living, Wellness'
	info['title'] = 'Regional Director of Nutrition Services'
	info['organization'] = 'Consulate Health Care'
	info['url'] = 'https://www.healthspansolutions.net'
	info['bio'] = 'Patricia Iorio has 35 years\' experience promoting nutrition and wellness. For the past dozen plus years she has focused on improving the lives of older adults through good nutrition and physical activity in the senior living industry. Serving as Corporate Director of Nutrition and Wellness for a large corporation she developed nutrition and wellness programs for 400 plus accounts across the U.S. Currently, as Regional Director of Nutrition Services for Consulate Health Care she oversee all aspects of the nutrition and dining services in 12 accounts in two states. Prior to joining Consulate Health Care Patricia founded Health Span Solutions where she serves as Executive Director to promote "wellness for life."'
	info['image_path'] = 'patricia_iorio.jpg'
	create_expert(info)

	info['email'] = 'info@triciard.com'
	info['first_name'] = 'Tricia'
	info['last_name'] = 'Stefankiewicz'
	info['temp_password'] = 'temp05'
	info['accreditations'] = 'MA, RDN, CNSC'
	info['areas_of_expertise'] = 'Weight and Disease Management, Wellness Promotion'
	info['title'] = 'Clinical Dietitian'
	info['organization'] = 'Hopsital of the University of Pennsylvania'
	info['url'] = 'http://www.triciard.com'
	info['bio'] = 'Tricia is a clinical dietitian at HUP and also has her own private practice. She has 9 years of clinical experience as well as 5 years of experience in adult weight management education with an emphasis on lifestyle behavior change. Tricia holds the Certificate for Adult Weight Management offered by the Academy of Nutrition and Dietetics.'
	info['image_path'] = 'tricia_s.jpg'
	create_expert(info)



	
