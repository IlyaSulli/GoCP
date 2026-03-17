def calculate_age(born) :
	today = date.today()
	try :
		birthday = born.replace(year = today.year)
	except ValueError :
		birthday = born.replace(year = today.year, month = born.month + 1, day = 1)
	if birthday > today :
		return today.year - born.year - 1
	else :
		return today.year - born.year


def calculate_age(born) :
	today = datetime.date.today()
	age_in_years = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
	months = (today.month - born.month - (today.day < born.day)) % 12
	age = today - born
	age_in_days = age.days
	if age_in_years > = 80 :
		return 80, 'years or older'
	if age_in_years > = 12 :
		return age_in_years, 'years'
	elif age_in_years > = 2 :
		half = 'and a half ' if months > 6 else ''
		return age_in_years, '%syears' % half
	elif months > = 6 :
		return months, 'months'
	elif age_in_days > = 14 :
		return age_in_days / 7, 'weeks'
	else :
		return age_in_days, 'days'

