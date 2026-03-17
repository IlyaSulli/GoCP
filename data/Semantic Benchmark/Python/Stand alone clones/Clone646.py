def daterange(start, end, step = datetime.timedelta(1)) :
	curr = start
	while curr < end :
		yield curr
		curr += step


def daterange(start, stop, step_days = 1) :
	current = start
	step = datetime.timedelta(step_days)
	if step_days > 0 :
		while current < stop :
			yield current
			current += step
	elif step_days < 0 :
		while current > stop :
			yield current
			current += step
	else :
		raise ValueError("daterange() step_days argument must not be zero")

