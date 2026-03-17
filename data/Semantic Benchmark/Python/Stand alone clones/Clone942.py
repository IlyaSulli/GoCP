def json_debug_handler(obj) :
	print ("object received:")
	print type(obj)
	print ("\n\n")
	if isinstance(obj, collections.Mapping) :
		for key, value in obj.iteritems() :
			if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
				value = json_debug_handler(value)
			obj [key] = convert(value)
	elif isinstance(obj, collections.MutableSequence) :
		for index, value in enumerate(obj) :
			if isinstance(value, (collections.Mapping, collections.MutableSequence)) :
				value = json_debug_handler(value)
			obj [index] = convert(value)
	return obj


def json_debug_handler(obj) :
	obj = obj.originalObject
	print ("object received:")
	print type(obj)
	print ("\n\n")
	if isinstance(obj, datetime.datetime) :
		return obj.isoformat()
	elif isinstance(obj, mDict) :
		return {'orig' : obj, 'attrs' : vars(obj)}
	elif isinstance(obj, mList) :
		return {'orig' : obj, 'attrs' : vars(obj)}
	else :
		return obj

