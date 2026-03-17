def get_cost(x) :
	t_zone = 720
	max_rate = 5.5
	rate = 0.0208
	duration = x ['t1']
	if duration < t_zone :
		if (duration * rate) > = max_rate :
			return max_rate
		else :
			return (duration * rate)
	else :
		if duration > = 720 :
			x = int(duration / 720)
			y = ((duration % 720) * rate)
			if y > = max_rate :
				return ((x * max_rate) + max_rate)
			else :
				return ((x * max_rate) + y)


def get_cost(df) :
	t_zone = 720
	max_rate = 5.5
	rate = 0.0208
	duration = df ['t1']
	ratecol = []
	for i in duration :
		if i < t_zone :
			if (i * rate) > = max_rate :
				ratecol.append(max_rate)
			else :
				ratecol.append(i * rate)
		else :
			if i > = 720 :
				x = int(i / 720)
				y = ((i % 720) * rate)
				if y > = max_rate :
					ratecol.append((x * max_rate) + max_rate)
				else :
					ratecol.append((x * max_rate) + y)
	return ratecol

