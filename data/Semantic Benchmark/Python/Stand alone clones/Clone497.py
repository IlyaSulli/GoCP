def rep_str(s, x, y) :
	result = ""
	skip = False
	if x in s :
		for i in range(len(s)) :
			if skip :
				skip = False
				continue
			if s [i : i + 2] == x :
				result += y
				skip = True
			else :
				result += s [i : i + 1]
		return result
	else :
		return s


def rep_str(string, search, replacement) :
	result = ''
	i = 0
	while i < len(string) :
		if string [i : i + len(search)] == search :
			result += replacement
			i += len(search)
		else :
			result += string [i]
			i += 1
	return result

