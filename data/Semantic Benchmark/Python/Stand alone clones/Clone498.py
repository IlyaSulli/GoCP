def rep_str(s, x, y) :
	while x in s :
		s = s [: s.index(x)] + y + s [s.index(x) + len(x) :]
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

