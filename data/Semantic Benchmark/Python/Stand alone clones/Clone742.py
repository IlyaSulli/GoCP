def package_contents(package_name) :
	file, pathname, description = imp.find_module(package_name)
	if file :
		raise ImportError('Not a package: %r', package_name)
	return set([os.path.splitext(module) [0] for module in os.listdir(pathname)
	if module.endswith(MODULE_EXTENSIONS)])


def package_contents(package_name) :
	spec = importlib.util.find_spec(package_name)
	if spec is None :
		return set()
	pathname = Path(spec.origin).parent
	ret = set()
	with os.scandir(pathname) as entries :
		for entry in entries :
			if entry.name.startswith('__') :
				continue
			current = '.'.join((package_name, entry.name.partition('.') [0]))
			if entry.is_file() :
				if entry.name.endswith(MODULE_EXTENSIONS) :
					ret.add(current)
			elif entry.is_dir() :
				ret.add(current)
				ret |= package_contents(current)
	return ret

