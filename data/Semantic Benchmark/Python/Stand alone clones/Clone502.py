def matched(str) :
	diffCounter = 0
	length = len(str)
	for i in range(length) :
		if str [i] == '(' :
			diffCounter += 1
		elif str [i] == ')' :
			diffCounter -= 1
	if diffCounter == 0 :
		return True
	else :
		return False


def matched(str) :
	count = 0
	for i in str :
		if i == "(" :
			count += 1
		elif i == ")" :
			count -= 1
		if count < 0 :
			return False
	return count == 0

