def age_in_years(from_date, to_date = datetime.date.today()) :
	if (DEBUG) :
		logger.debug("def age_in_years(from_date='%s', to_date='%s')" % (from_date, to_date))
	if (from_date > to_date) :
		logger.debug('Swapping dates ...')
		tmp = from_date
		from_date = to_date
		to_date = tmp
	age_delta = to_date.year - from_date.year
	month_delta = to_date.month - from_date.month
	day_delta = to_date.day - from_date.day
	if (DEBUG) :
		logger.debug("Delta's are : %i  / %i / %i " % (age_delta, month_delta, day_delta))
	if (month_delta > 0 or (month_delta == 0 and day_delta > = 0)) :
		return age_delta
	return (age_delta - 1)


def age_in_years(from_date, to_date, leap_day_anniversary_Feb28 = True) :
	age = to_date.year - from_date.year
	try :
		anniversary = from_date.replace(year = to_date.year)
	except ValueError :
		assert from_date.day == 29 and from_date.month == 2
		if leap_day_anniversary_Feb28 :
			anniversary = datetime.date(to_date.year, 2, 28)
		else :
			anniversary = datetime.date(to_date.year, 3, 1)
	if to_date < anniversary :
		age -= 1
	return age

