def json_debug_handler(obj) :
	print ("object received:")
	print (type(obj))
	print ("\n\n")
	if isinstance(obj, datetime.datetime) :
		return obj.isoformat()
	elif isinstance(obj, MStuff) :
		attrs = {}
		for key in obj.__dict__ :
			if not (key.startswith("_") or key == "content") :
				attrs [key] = obj.__dict__ [key]
		return {'orig' : obj.content, 'attrs' : attrs}
	else :
		return None


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

