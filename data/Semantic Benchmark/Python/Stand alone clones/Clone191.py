def add_months(d, months) :
	for i in range(4) :
		day = d.day - i
		try :
			return d.replace(day = day).replace(year = d.year + int(months) / / 12).replace(month = (d.month + int(months)) % 12)
		except :
			pass
	raise Exception("should not happen")


def add_months(date, months) :
	months_count = date.month + months
	year = date.year + int(months_count / 12)
	month = (months_count % 12)
	if month == 0 :
		month = 12
	day = date.day
	last_day_of_month = calendar.monthrange(year, month) [1]
	if day > last_day_of_month :
		day = last_day_of_month
	new_date = datetime.date(year, month, day)
	return new_date

