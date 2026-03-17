def sumvars(x, y, z, d = None) :
	s = x
	if not d is None :
		d ['first_step'] = s
	s += y
	if not d is None :
		d ['second_step'] = s
	s += z
	return s


def sumvars(x, y, z, mode = 'default') :
	d = {}
	s = x
	d ['first_step'] = s
	s += y
	d ['second_step'] = s
	s += z
	d ['final'] = s
	if mode == 'default' :
		return s
	else :
		return d

