def smart_func(terms) :
	params = []
	for n in range(terms) :
		params.append(2 * n * np.pi)
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
	return func


def smart_func(num_terms) :
	template = dedent('''
	def func(t, freq, offset, a0, b0, {params}):
	ang = 2.*np.pi*freq*t
	sin_ang = np.sin(ang)
	cos_ang = np.cos(ang)
	return (a0 + b0
	{terms}
	+ offset)
	''')
	indent = ' ' * 12
	params, terms = [], []
	for i in range(1, num_terms) :
		params.append('a{i}, b{i}'.format(i = i))
		terms.append((indent + '+ a{i}*sin_ang\n' +
		indent + '+ b{i}*cos_ang').format(i = i))
	src_code = template.format(params = ', '.join(params), terms = '    \n'.join(terms))
	print ('Dynamically created function of {} terms:'.format(num_terms))
	print (src_code)
	exec (src_code, globals(), locals())
	return locals() ['func']

