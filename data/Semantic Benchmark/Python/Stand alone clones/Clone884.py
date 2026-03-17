def specialMultiplication(n) :
	to_process = []
	result = 1
	if n > = 2 :
		to_process.append(n)
		while to_process :
			n = to_process.pop()
			result *= n
			if n > = 3 :
				to_process.append(n - 1)
				if n > = 4 :
					to_process.append(n - 2)
	return result


def specialMultiplication(max_n) :
	a = b = 1
	for n in range(1, max_n + 1) :
		a, b = b, a * b * n
	return b

