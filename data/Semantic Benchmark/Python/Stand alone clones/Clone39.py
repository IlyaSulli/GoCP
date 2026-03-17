def num_subsequences(seq, sub) :
	if not sub :
		return 1
	elif not seq :
		return 0
	result = num_subsequences(seq [1 :], sub)
	if seq [0] == sub [0] :
		result += num_subsequences(seq [1 :], sub [1 :])
	return result


def num_subsequences(seq, sub) :
	m, n = len(seq), len(sub)
	table = [0] * n
	for i in xrange(m) :
		previous = 1
		for j in xrange(n) :
			current = table [j]
			if seq [i] == sub [j] :
				table [j] += previous
			previous = current
	return table [n - 1] if n else 1

