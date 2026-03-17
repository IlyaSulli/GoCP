def matched(s) :
	p_list = []
	for i in range(0, len(s)) :
		if s [i] == '(' :
			p_list.append('(')
		elif s [i] == ')' :
			if not p_list :
				return False
			else :
				p_list.pop()
	if not p_list :
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

