def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		risk = "Low"
	elif bmi < 22 and age > = 45 :
		risk = "Medium"
	elif bmi > = 22 and age < 45 :
		risk = "Medium"
	elif bmi > = 22 and age > = 45 :
		risk = "High"
	else :
		risk = "Unknown"
	return risk


def bmi_risk(bmi, age) :
	if bmi < 22 and age < 45 :
		return "Low"
	if bmi > = 22 and age > = 45 :
		return "High"
	return "Medium"

