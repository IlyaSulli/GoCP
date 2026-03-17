def function1(n, d) :
	if n / 2 in d :
		d [n] = d [n / 2] + 1
		return
	if n not in d :
		length = 0
		temp = n
		while temp > 1 :
			if temp % 2 == 0 :
				temp //= 2
			else :
				temp = 3 * temp + 1
			length += 1
			if temp in d :
				length += d [temp]
				break
		d [n] = length


def function1(n, d) :
	if n % 2 == 0 and n / / 2 in d :
		d [n] = d [n / / 2] + 1
	if n not in d :
		temp = n
		intermediates = []
		while temp > 1 :
			if temp % 2 == 0 :
				temp //= 2
			else :
				temp = 3 * temp + 1
			if temp in d :
				d [n] = res = d [temp] + len(intermediates) + 1
				for i, temp in enumerate(intermediates, 1) :
					d [temp] = res - i
				return res
			else :
				intermediates.append(temp)
	return d [n]

