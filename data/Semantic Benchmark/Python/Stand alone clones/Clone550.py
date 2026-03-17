def is_member(x) :
	a = [1, 5, 3, 9, 4, 100]
	for i in a :
		if i == x :
			return "True"
	return "False"


def is_member(x) :
	a = [1, 5, 3, 9, 4, 100]
	i = 0
	found = False
	while found == False :
		if i > = len(a) :
			return False
		if x == a [i] :
			found = True
			break
		i += 1
	if found == True :
		return "True"
	else :
		return "False"

