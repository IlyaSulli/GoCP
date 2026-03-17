def get_user_attributes(cls, exclude_methods = True) :
	base_attrs = dir(type('dummy', (object,), {}))
	this_cls_attrs = dir(cls)
	res = []
	for attr in this_cls_attrs :
		if base_attrs.count(attr) or (callable(getattr(cls, attr)) and exclude_methods) :
			continue
		res += [attr]
	return res


def get_user_attributes(cls) :
	boring = dir(type('dummy', (object,), {}))
	attrs = {}
	bases = reversed(inspect.getmro(cls))
	for base in bases :
		if hasattr(base, '__dict__') :
			attrs.update(base.__dict__)
		elif hasattr(base, '__slots__') :
			if hasattr(base, base.__slots__ [0]) :
				for item in base.__slots__ :
					attrs [item] = getattr(base, item)
			else :
				attrs [base.__slots__] = getattr(base, base.__slots__)
	for key in boring :
		del attrs ['key']
	return attrs

