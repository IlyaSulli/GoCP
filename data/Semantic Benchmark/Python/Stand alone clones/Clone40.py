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
	m, n = len(seq) + 1, len(sub) + 1
	table = [[0] * n for i in xrange(m)]
	def count(iseq, isub) :
		if not isub :
			return 1
		elif not iseq :
			return 0
		return (table [iseq - 1] [isub] +
		(table [iseq - 1] [isub - 1] if seq [m - iseq - 1] == sub [n - isub - 1] else 0))
	for row in xrange(m) :
		for col in xrange(n) :
			table [row] [col] = count(row, col)
	return table [m - 1] [n - 1]

