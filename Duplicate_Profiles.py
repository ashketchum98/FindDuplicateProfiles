from fuzzywuzzy import fuzz

class Profile():

	def __init__(self, first_name, last_name, date_of_birth, class_year, email_field):
		self.first_name = first_name
		self.last_name  = last_name
		self.date_of_birth = date_of_birth
		self.class_year = class_year
		self.email_field = email_field

	def __str__(self):
		return self.first_name + " " + self.last_name

def duplicate_profile(profiles, fields):

	output_profiles = {"profiles": profiles, "total_match_score": 0, "matching_attributes": [], "non_matching_attributes": [], "ignored_attributes": []}

	total_score = 0
	profile1, profile2 = profiles[0], profiles[1]

	first_name_ratio = fuzz.ratio(profile1.first_name, profile2.first_name)
	last_name_ratio = fuzz.ratio(profile1.last_name, profile2.last_name)
	email_ratio = fuzz.ratio(profile1.email_field, profile2.email_field)

	if (first_name_ratio + last_name_ratio + email_ratio)//3 > 80:
		output_profiles["matching_attributes"].extend(["first_name", "last_name", "email_field"])
		total_score += 1
	else:
		output_profiles["non_matching_attributes"].extend(["first_name", "last_name", "email_field"])

	dob_ratio = fuzz.ratio(profile1.date_of_birth, profile2.date_of_birth)
	if profile1.date_of_birth is not None and profile2.date_of_birth is not None:
		if dob_ratio == 100:
			total_score += 1
			output_profiles["matching_attributes"].append("date_of_birth")
		else:
			total_score -= 1
			output_profiles["non_matching_attributes"].append("date_of_birth")
	else:
		output_profiles["ignored_attributes"].append("date_of_birth")

	class_year_ratio = fuzz.ratio(profile1.class_year, profile2.class_year)
	if profile1.class_year is not None and profile2.class_year is not None:
		if class_year_ratio == 100:
			total_score += 1
			output_profiles["matching_attributes"].append("class_year")
		else:
			total_score -= 1
			output_profiles["non_matching_attributes"].append("class_year")
	else:
		output_profiles["ignored_attributes"].append("class_year")

	output_profiles["total_match_score"] = total_score

	return output_profiles


profile_obj1 = Profile("Rahul", "Singh", "10/11/1998", None, "rahul@gmail.com")
profile_obj2 = Profile("Rahul", "Singh", "12/01/1999", None, "rksingh@gmail.com")


result = duplicate_profile([profile_obj1, profile_obj2], ["first_name", "last_name", "email_field", "date_of_birth", "class_year"])

print(profile_obj1)
print(profile_obj2)
print(result)








