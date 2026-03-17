def change_keys(obj) :
	new_obj = obj
	for k in new_obj :
		if hasattr(obj [k], '__getitem__') :
			change_keys(obj [k])
		if '.' in k :
			obj [k.replace('.', '$')] = obj [k]
			del obj [k]


def change_keys(obj, convert) :
	if isinstance(obj, (str, int, float)) :
		return obj
	if isinstance(obj, dict) :
		new = obj.__class__()
		for k, v in obj.items() :
			new [convert(k)] = change_keys(v, convert)
	elif isinstance(obj, (list, set, tuple)) :
		new = obj.__class__(change_keys(v, convert) for v in obj)
	else :
		return obj
	return new

