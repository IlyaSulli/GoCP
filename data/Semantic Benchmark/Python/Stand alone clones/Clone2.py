def purge(dir, pattern) :
	for f in os.listdir(dir) :
		if re.search(pattern, f) :
			os.remove(os.path.join(dir, f))


def purge(dir, pattern, inclusive = True) :
	regexObj = re.compile(pattern)
	for root, dirs, files in os.walk(dir, topdown = False) :
		for name in files :
			path = os.path.join(root, name)
			if bool(regexObj.search(path)) == bool(inclusive) :
				os.remove(path)
		for name in dirs :
			path = os.path.join(root, name)
			if len(os.listdir(path)) == 0 :
				os.rmdir(path)

