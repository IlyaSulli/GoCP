def todict(obj, classkey = None) :
	if isinstance(obj, dict) :
		data = {}
		for (k, v) in obj.items() :
			data [k] = todict(v, classkey)
		return data
	elif hasattr(obj, "_ast") :
		return todict(obj._ast())
	elif hasattr(obj, "__iter__") and not isinstance(obj, str) :
		return [todict(v, classkey) for v in obj]
	elif hasattr(obj, "__dict__") :
		data = dict([(key, todict(value, classkey)) for key, value in obj.__dict__.items()
		if not callable(value) and not key.startswith('_')])
		if classkey is not None and hasattr(obj, "__class__") :
			data [classkey] = obj.__class__.__name__
		return data
	else :
		return obj


def todict(obj) :
	if isinstance(obj, basestring) :
		return obj
	elif isinstance(obj, dict) :
		return dict((key, todict(val)) for key, val in obj.items())
	elif isinstance(obj, collections.Iterable) :
		return [todict(val) for val in obj]
	elif hasattr(obj, '__dict__') :
		return todict(vars(obj))
	elif hasattr(obj, '__slots__') :
		return todict(dict((name, getattr(obj, name)) for name in getattr(obj, '__slots__')))
	return obj

