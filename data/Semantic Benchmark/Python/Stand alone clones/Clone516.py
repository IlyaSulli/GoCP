def merge(dict1, dict2) :
	for k in dict1.keys() - dict2.keys() :
		yield (k, dict1 [k])
	for k in dict2.keys() - dict1.keys() :
		yield (k, dict2 [k])
	for k in dict1.keys() & dict2.keys() :
		yield (k, dict(merge(dict1 [k], dict2 [k])))


def merge(a, b, path = []) :
	for key in b :
		if key in a :
			if isinstance(a [key], dict) and isinstance(b [key], dict) :
				merge(a [key], b [key], path + [str(key)])
			elif a [key] == b [key] :
				pass
			else :
				raise Exception('Conflict at `{path}\''.format(path = '.'.join(path + [str(key)])))
		else :
			if isinstance(b [key], dict) :
				a [key] = clone_dict(b [key])
			else :
				a [key] = b [key]
	return a

