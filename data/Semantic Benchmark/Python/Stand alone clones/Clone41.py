def num_subsequences(seq, sub) :
	m, n = len(seq), len(sub)
	@ lru_cache(maxsize = None)
	def count(i, j) :
		if j == n :
			return 1
		elif i == m :
			return 0
		return count(i + 1, j) + (count(i + 1, j + 1) if seq [i] == sub [j] else 0)
	return count(0, 0)


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

