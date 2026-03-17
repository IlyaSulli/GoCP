def __call__(self, * args, ** kwargs) :
	obj = type.__call__(self)
	obj.defaults = _DEFAULTS [obj.__class__.__name__]
	for klass in obj.__class__.__bases__ :
		if klass.__name__ in _DEFAULTS :
			obj.defaults.update(_DEFAULTS [klass.__name__])
	return obj


def __call__(self, * args, ** kwargs) :
	obj = type.__call__(self)
	for klass in obj.__class__.__mro__ :
		if klass == obj.__class__ or klass == Base or not issubclass(klass, Base) :
			continue
		if hasattr(klass, 'DEFAULTS') :
			d = klass.DEFAULTS.copy()
			d.update(obj.DEFAULTS)
			obj.DEFAULTS = d
	return obj

