def R(A) :
	if (0 in A) - 1 : yield A; return
	def H(i) : h = set(A [j] for j in r if j / 9 == i / 9 or j % 9 == i % 9 or j / 27 == i / 27 and j % 9 / 3 == i % 9 / 3); return len(h), h, i
	l, h, i = max(H(i) for i in r if not A [i])
	for j in r [1 : 10] :
		if (j in h) - 1 :
			A [i] = j
			for S in R(A) : yield S
		A [i] = 0


def R(A) :
	z = {}
	for i in r :
		if A [i] ! = 0 : continue
		h = {}
		for j in r : h [A [j] if j / 9 == i / 9 or j % 9 == i % 9 or j / 27 == i / 27 and j % 9 / 3 == i % 9 / 3 else 0] = 1
		z [9 - len(h)] = h, i
	for l, (h, i) in sorted(z.items(), cmp, lambda x : x [0]) :
		for j in s :
			if j not in h :
				A [i] = j
				if R(A) : return A
		A [i] = 0; return []
	return A

