from mainapp.models import *

def add_expert_profiles():
	
	# FIRST - CREATE ACCREDITATIONS

	# Delete all existing accreditations
	Accreditation.objects.all().delete()
	Expert_Profile_Accreditation_Rel.objects.all().delete()

	# Add all accreditations
	RD = Accreditation(name="RD")
	RD.save();

	LD = Accreditation(name="LD")
	LD.save();

	PhD = Accreditation(name="PhD")
	PhD.save();

	MA = Accreditation(name="MA")
	MA.save();

	MS = Accreditation(name="MS")
	MS.save();

	LDN = Accreditation(name="LDN")
	LDN.save();

	RDN = Accreditation(name="RDN")
	RDN.save();

	RN = Accreditation(name="RN")
	RN.save();

	MPH = Accreditation(name="MPH")
	MPH.save();

	# SECOND - Add Areas of Expertise
	Area_Of_Expertise.objects.all().delete()
	Expert_Profile_Expertise_Rel.objects.all().delete()

	obesity = Area_Of_Expertise(name="Obesity")
	obesity.save()

	diabetes = Area_Of_Expertise(name="Diabetes")
	diabetes.save()

	physiology = Area_Of_Expertise(name="Physiology")
	physiology.save()

	energy_balance = Area_Of_Expertise(name="Energy Balance")
	energy_balance.save()

	eating_disorders = Area_Of_Expertise(name="Eating Disorders")
	eating_disorders.save()

	chronic_diseases = Area_Of_Expertise(name="Chronic Diseases")
	chronic_diseases.save()

	general_nutrition = Area_Of_Expertise(name="General Nutrition")
	general_nutrition.save()

	nutrition_through_lifecycle = Area_Of_Expertise(name="Nutrition through the Lifecycle")
	nutrition_through_lifecycle.save()

	food_allergies = Area_Of_Expertise(name="Food Allergies")
	food_allergies.save()

	gluten_free = Area_Of_Expertise(name="Gluten Free")
	gluten_free.save()

	nutrition_therapy = Area_Of_Expertise(name="Nutrition Therapy")
	nutrition_therapy.save()

	healthy_living = Area_Of_Expertise(name="Healthy Living")
	healthy_living.save()

	nutritional_biochemistry = Area_Of_Expertise(name="Nutritional Biochemistry")
	nutritional_biochemistry.save()

	inflammation = Area_Of_Expertise(name="Nutritional Adaptations to Inflammation")
	inflammation.save()

	juicing = Area_Of_Expertise(name="Juicing")
	juicing.save()

	micronutrient_deficiencies = Area_Of_Expertise(name="Micronutrient Deficiencies")
	micronutrient_deficiencies.save()

	weight_loss = Area_Of_Expertise(name="Weight Loss")
	weight_loss.save()

	micronutrient_biochemistry = Area_Of_Expertise(name="Micronutrient Biochemistry")
	micronutrient_biochemistry.save()

	lipid_metabolism = Area_Of_Expertise(name="Lipid Metabolism")
	lipid_metabolism.save()

	dietary_guidelines = Area_Of_Expertise(name="Dietary Guidelines")
	dietary_guidelines.save()

	variability = Area_Of_Expertise(name="Inter-individual Variability")
	variability.save()

	weight_management_pediatrics = Area_Of_Expertise(name="Weight Management Pediatrics")
	weight_management_pediatrics.save()

	public_health = Area_Of_Expertise(name="Public Health")
	public_health.save()

	med_diet = Area_Of_Expertise(name="Mediterranean-style Diets")
	med_diet.save()

	weight_management = Area_Of_Expertise(name="Weight Management")
	weight_management.save()

	community_nutrition = Area_Of_Expertise(name="Community Nutrition")
	community_nutrition.save()

	nutrition_in_minorities = Area_Of_Expertise(name="Nutrition in Minority Populations")
	nutrition_in_minorities.save()

	genetics = Area_Of_Expertise(name="Genetics")
	genetics.save()

	neuroendocrine = Area_Of_Expertise(name="Neuroendocrine Systems")
	neuroendocrine.save()

	exercise = Area_Of_Expertise(name="Exercise")
	exercise.save()

	vitamins_minerals = Area_Of_Expertise(name="Vitamins and Minerals")
	vitamins_minerals.save()





	# THIRD - Populate with expert profiles

	# Delete all existing data
	Expert_Profile.objects.all().delete()

	# Helper function to create profiles
	def create_profile(first_name, last_name, title, organization, bio, website, accreditations, expertise, image_path):
		# Create Expert_Profile
		expert_profile = Expert_Profile(first_name=first_name,last_name=last_name,title=title,organization=organization,bio=bio,website=website, image_path=image_path)
		expert_profile.save()

		# Create Accreditation Relationships
		for a in accreditations:
			rel_a = Expert_Profile_Accreditation_Rel(expert_profile=expert_profile, accreditation=a)
			rel_a.save()

		# Create Expertise Relationships
		for e in expertise:
			rel_e = Expert_Profile_Expertise_Rel(expert_profile=expert_profile,area_of_expertise=e)
			rel_e.save()


	# Bart de Jonghe
	create_profile("Bart", "de Jonghe", "Associate Professor of Nutrition", "University of Pennsylvania", 'Dr. De Jonghe is an Assistant Professor of Nursing and obesity researcher in the University of Pennsylvania\'s School of Nursing. Dr. De Jonghe teaches "Nutrition: Science and Applications" (NURS 112), the introductory course in Penn\'s Nutrition Minor program. Dr. De Jonghe\'s research focuses on the nutritional, physiological, neuronal, and cellular signaling controls of energy balance with relevance to obesity, type 2 diabetes, and chemotherapy-induced nausea and vomiting. Dr. De Jonghe received his Ph.D. in Nutritional Sciences from the Pennsylvania State University in 2006, after which he entered a two-year Postdoctoral Fellowship in Neurophysiology at the Monell Chemical Senses Center to study nausea, vomiting and malaise.' , "http://www.nursing.upenn.edu/faculty/profile.asp?pid=2960", [PhD], [obesity,energy_balance,eating_disorders],"bart_de_jonghe.jpg")

	# Mary Zeoli
	create_profile("Mary", "Zeoli", "Registered Dietitian, School Nurse", "", 'Mary is a Registered Dietitan and Registered Nurse passionate about using nutrition to enhance health through the lifespan and minimize the effects of chronic disease. She does nutrition consulting in a nursing home, works a school system, and applies nutrition concepts in the context of food catering and event organization. Mary received her BS in Food and Nutrition from SUNY Plattsburgh and her MS in Nutrition and Exercise from NYU.', "", [RD, MS, RN], [chronic_diseases, general_nutrition, nutrition_through_lifecycle],"gray_circle.jpg")

	# Melissa Foor
	create_profile("Melissa", "Foor", "Registered Dietitian", "", 'Melissa is a Registered Dietitian Nutrionist and completed her dietetic internship at the St. Anthony\'s Memorial Hospital. She completed her Master\'s thesis on the effect of dark chocolate on blood pressure at the Eastern Illinois University. She will begin working at OrthoIndy as a Clinical Nutrition Manager in December.', "", [RDN], [food_allergies, gluten_free, general_nutrition],"melissa_foor.jpg")

	# Flavia Herzog Liebel
	create_profile("Flavia", "Herzog Liebel", "Registered Dietitian", "CEO, Therapeutic Nutrition", '', "", [MA, RD, LDN], [eating_disorders, weight_management_pediatrics, nutrition_therapy],"flavia_herzog_2.jpg")

	# Matam Vijay-Kumar
	create_profile("Matam", "Vijay-Kumar", "Professor and Researcher", "Pennsylvania State University", 'Dr. Vijay-Kumar is an Assistant Professor and Researcher at the Pennsylvania State University\'s Department of Nutritional Sciences. Dr. Vijay-Kumar\'s areas of interest include Host Metabolic Adaptations to Inflammation, Innate Immunity-Gut Microbiotal Interactions in Metabolic Diseases, and Iron Homeostasis in Inflammaton. He received his Ph.D. in Biochemistry at the Central Food Technological Research Institute in Mysore, India.', "http://nutrition.hhd.psu.edu/directory/Bio.aspx?id=VijayKumar", [PhD], [nutritional_biochemistry, inflammation],"matam_vijay_kumar.jpg")

	# Steve Dupont
	create_profile("Steve", "Dupont", "Clinical Dietitian", "University of Alabama at Birmingham (UAB) Hospital", 'A veritable journeyman and humble rider of the space-time continuum, Steve has pursued several passions during his career. After graduating from Vanderbilt University (1996) with a degree in English/Creative Writing, he enjoyed brief success as a freelance journalist and author of two books -- including Therein Lies the Problem, a novel. Then, after studying nutrition independently for several years, he returned to school and ultimately completed a dietetic internship program at UAB. He has worked as a clinical dietitian at UAB Hospital since 2012. He has also been in private practice since 2013 and started a podcast in 2014 called Cutting Through the Nutrition Nonsense. Additionally, Steve has appeared on NPR and Fox News as a nutrition spokesman. He lives in beautiful Birmingham, Alabama with his wife and two children.', "http://www.stevedupont.com/", [RD, LD], [weight_loss, micronutrient_deficiencies, juicing, diabetes],"steve_dupont.jpg")

	# Alison Borkowska
	create_profile("Alison", "Borkowska", "Instructor", "The Pennsylvania State University, Department of Nutritional Sciences", 'Dr. Borkowska teaches undergraduate nutrition at Penn State. She came by way of Massachusetts General Hospital, where she was working in research pertaining to HIV infection and cardiovascular disease. Prior to her appointment there, she worked at the University of Copenhagen in the Department of Biology. There she studied adipose physiology. She completed her PhD at the University of California, Davis in Nutritional Biology. Her dissertation work focused on targeted metabolomics in the context of omega-3 fatty acid supplementation.', "http://nutrition.hhdev.psu.edu/directory/Bio.aspx?id=AlisonBorkowska", [PhD], [lipid_metabolism, weight_loss, variability, micronutrient_biochemistry, dietary_guidelines],"alison_borkowska.jpg")	

	# Andrew Lakanen
	create_profile("Andrew", "Lakanen", "Nutritionist and Statistician", "St. Paul Radiology", 'Andrew is a Registered Dietitian Nutritionist and Statistician at St. Paul Radiology. He\'s engaging in the MediVat Study, a 12-month clinical trial investigating the effects of the Mediterranean-style Diet on visceral fat. In addition to research, Andrew focuses on Public Health and Health Promotion.', "", [MS, RDN], [public_health, med_diet],"andrew_lakanen.jpg")	

	# Zubaida Qamar
	create_profile("Zubaida", "Qamar", "Doctoral Student", "Texas A&M University", 'Zubaida is a PhD student at Texas A&M University with her dissertation focus in nutrition education programs in minority populations using web-based resources. She is passionate about preventative nutrition and using nutrition to obtain optimal health at all stages of life along with prevention of diseases. She loves to teach and enjoys her job as a teaching assistant. She received her B.S. in Dietetics with a concentration in pre-medicine from State University of New York (SUNY) at Oneonta and her M.S. in Nutritional Sciences from Texas A&M University.', "", [MS], [general_nutrition, nutrition_in_minorities, community_nutrition, weight_management],"zubaida_qamar.jpg")	

	# Deborah Good
	create_profile("Deborah", "Good", "Associate Professor", "Virginia Tech, Department of Human Nutrition, Foods and Exercise", 'Dr. Deborah J. Good obtained her Ph.D. in Molecular and Cellular Biology from Northwestern University in 1992, where she was awarded a patent for her work to identify a naturally-occurring inhibitor of angiogenesis, thrombospondin. In 1997, Dr. Good accepted a position for a tenure-track Assistant Professor in the Department of Veterinary and Animal Sciences at the University of Massachusetts-Amherst, where she was awarded tenure in 2003. She moved to Virginia Tech in 2006, and since starting her independent laboratory, she has secured over 1.77 million dollars in awards and published over 50 journal articles and book chapters on the genetics of body weight regulation. Her research program is recognized internationally in the area of the molecular, genetic, and neuroendocrine control of body weight. Outside of her research and work on her lab, she plays in a community band, loves animals, and cooks with her family.', "https://www.hnfe.vt.edu/People/faculty/Biographies/good.html", [PhD], [obesity, genetics, vitamins_minerals, neuroendocrine, exercise],"deborah_good.jpg")	

	# Patricia Iorio
	# create_profile("Patricia", "Iorio", "Doctoral Student", "Texas A&M University", 'Zubaida is a PhD student at Texas A&M University with her dissertation focus in nutrition education programs in minority populations using web-based resources. She is passionate about preventative nutrition and using nutrition to obtain optimal health at all stages of life along with prevention of diseases. She loves to teach and enjoys her job as a teaching assistant. She received her B.S. in Dietetics with a concentration in pre-medicine from State University of New York (SUNY) at Oneonta and her M.S. in Nutritional Sciences from Texas A&M University.', "", [MS], [general_nutrition, nutrition_in_minorities, community_nutrition, weight_management],"zubaida_qamar.jpg")	


	# # Alison Borkowska
	# create_profile("Rachel", "Hudes", "Professor and Researcher", "Pennsylvania State University", '', "http://www.stevedupont.com/", [MS, RD, LDN], [],"matam_vijay_kumar.png")

