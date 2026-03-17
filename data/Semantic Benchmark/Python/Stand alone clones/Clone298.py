def extendedString(string1, string2) :
	x = string1
	y = string2
	if len(x) < len(y) :
		x = x + x [- 1] * (len(y) - len(x))
	elif len(x) > len(y) :
		y = y + y [- 1] * (len(x) - len(y))
	return "".join(i for j in zip(x, y) for i in j)


def extendedString(string1, string2) :
	if len(string1) < = len(string2) :
		x = string1
		y = string2
	else :
		x = string2
		y = string1
	z = ""
	for i in range(len(x)) :
		z += x [i]
		z += y [i]
	if i < len(y) :
		for j in range(i + 1, len(y)) :
			z += x [i]
			z += y [j]
	return z

