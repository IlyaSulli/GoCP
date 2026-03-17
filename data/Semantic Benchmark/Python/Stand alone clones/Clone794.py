def recursiveHalfString(s, offset = 0) :
	half, odd = divmod(len(s), 2)
	assert (not odd)
	if not s or offset > half :
		return True
	if s [offset] ! = s [half + offset] :
		return False
	return recursiveHalfString(s, offset + 1)


def recursiveHalfString(s) :
	if s == '' :
		return True
	if (len(s)) % 2 == 0 :
		if s [0] ! = s [(len(s) / 2)] :
			return False
		else :
			left = s [1 : len(s) / 2]
			right = s [(len(s) / 2) + 1 : len(s)]
			return recursiveHalfString(left + right)
	else :
		return "Error: odd string"

