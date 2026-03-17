def myfunc(lst) :
	ret = []
	a = b = lst [0]
	for el in lst [1 :] :
		if el == b + 1 :
			b = el
		else :
			ret.append(a if a == b else (a, b))
			a = b = el
	ret.append(a if a == b else (a, b))
	return ret


def myfunc(l) :
	r = []
	p = q = None
	for x in l + [- 1] :
		if x - 1 == q :
			q += 1
		else :
			if p :
				if q > p :
					r.append('%s-%s' % (p, q))
				else :
					r.append(str(p))
			p = q = x
	return '(%s)' % ', '.join(r)

