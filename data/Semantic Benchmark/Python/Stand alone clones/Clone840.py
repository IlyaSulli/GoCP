def problem_a(n, answer = None) :
	answer = [n] if answer is None else answer
	if n == 1 :
		return answer
	elif n % 2 == 0 :
		n = n / 2
		answer.append(n)
	else :
		n = n * 3 + 1
		answer.append(n)
	return problem_a(n, answer)


def problem_a(n) :
	yield n
	if n == 1 :
		return
	elif n % 2 == 0 :
		x = n / 2
	else :
		x = n * 3 + 1
	for y in problem_a(x) :
		yield y

