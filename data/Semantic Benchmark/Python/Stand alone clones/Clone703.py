def change_keys(obj) :
	new_obj = obj
	for k in new_obj :
		if hasattr(obj [k], '__getitem__') :
			change_keys(obj [k])
		if '.' in k :
			obj [k.replace('.', '$')] = obj [k]
			del obj [k]


def change_keys(obj, convert) :
	if isinstance(obj, dict) :
		new = {}
		for k, v in obj.iteritems() :
			new [convert(k)] = change_keys(v, convert)
	elif isinstance(obj, list) :
		new = []
		for v in obj :
			new.append(change_keys(v, convert))
	else :
		return obj
	return new

