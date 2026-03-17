def wrapped(mod) :
	name = getattr(mod, 'filename', None)
	if name is None :
		return True
	name = join(realpath(dirname(name)), '')
	if not name.startswith(prefix) :
		return True
	for p in all_prefix :
		if name.startswith(p) :
			return True
	return False


def wrapped(src, * args, ** kwargs) :
	name = src
	if not is_dir :
		name = dirname(src)
	name = join(realpath(name), '')
	keep = True
	for prefix, sub_prefixes in prefixes.iteritems() :
		if name == prefix :
			continue
		if name.startswith(prefix) :
			keep = False
			for sub_prefix in sub_prefixes :
				if name.startswith(sub_prefix) :
					keep = True
					break
	if keep :
		return fn(src, * args, ** kwargs)
	return []

