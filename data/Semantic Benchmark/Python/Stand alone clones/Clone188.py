def sum_numbers(s) :
	def convert_s_to_val(s) :
		if s :
			return float(s)
		else :
			return 0
	sum = 0
	current = ''
	for c in s :
		if c.isspace() :
			sum += convert_s_to_val(current)
			current = ''
		else :
			current = current + c
	sum += convert_s_to_val(current)
	return sum


def sum_numbers(s) :
	sm = i = 0
	while i < len(s) :
		t = ""
		while i < len(s) and not s [i].isspace() :
			t += s [i]
			i += 1
		if t :
			sm += float(t)
		else :
			i += 1
	return sm

