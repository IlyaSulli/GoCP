def func(t, freq, offset, * args) :
	an = []
	bn = []
	for i in range(len(args)) :
		if i % 2 == 0 :
			an.append(args [i])
		else :
			bn.append(args [i])
	result = 0
	pairs = zip(an, bn)
	for (q, ab) in zip(params, pairs) :
		ai, bi = ab
		result += ai * np.sin(q * freq * t) + bi * np.cos(q * freq * t)
	return result


def func(t, freq, offset, * params) :
	result = 0
	for (a, b) in zip(params) :
		result += np.sin(a * freq * t) + np.cos(b * freq * t)
	return result

