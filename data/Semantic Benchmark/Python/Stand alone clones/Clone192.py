def add_months(d, months) :
	for i in range(4) :
		day = d.day - i
		try :
			return d.replace(day = day).replace(year = d.year + int(months) / / 12).replace(month = (d.month + int(months)) % 12)
		except :
			pass
	raise Exception("should not happen")


def add_months(start_date, months) :
	import calendar
	year = start_date.year + (months / 12)
	month = start_date.month + (months % 12)
	day = start_date.day
	if month > 12 :
		month = month % 12
		year = year + 1
	days_next = calendar.monthrange(year, month) [1]
	if day > days_next :
		day = days_next
	return start_date.replace(year, month, day)

