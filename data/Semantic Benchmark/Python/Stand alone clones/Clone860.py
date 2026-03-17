def search(plugindir) :
	for root, dirs, files in os.walk(plugindir) :
		for fname in files :
			modname = os.path.splitext(fname) [0]
			try :
				module = imp.load_source(modname, os.path.join(root, fname))
			except Exception : continue


def search(base) :
	for root, dirs, files in os.walk('.') :
		candidates = [fname for fname in files if fname.endswith('.py')
		and not fname.startswith('__')]
		classList = []
		if candidates :
			for c in candidates :
				modname = os.path.splitext(c) [0]
				try :
					module = __import__(modname)
				except (ImportError, NotImplementedError) :
					continue
				for cls in dir(module) :
					cls = getattr(module, cls)
					if (inspect.isclass(cls)
					and inspect.getmodule(cls) == module
					and issubclass(cls, base)) :
						classList.append(cls)
		print (classList)

