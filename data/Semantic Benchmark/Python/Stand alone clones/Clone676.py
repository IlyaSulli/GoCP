def char_first_index(s, c, index = 0) :
	if len(s) == index :
		return None
	if s [index] == c :
		return index
	return char_first_index(s, c, index + 1)


def char_first_index(s, c) :
	if len(s) == 0 :
		return None
	elif s [0] == c :
		return 0
	else :
		count = char_first_index(s [1 :], c)
		if count ! = None :
			return count + 1
		else :
			return None

