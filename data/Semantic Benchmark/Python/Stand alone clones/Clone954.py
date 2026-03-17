def todict(obj) :
	data = {}
	for key, value in obj.__dict__.iteritems() :
		try :
			data [key] = todict(value)
		except AttributeError :
			data [key] = value
	return data


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

