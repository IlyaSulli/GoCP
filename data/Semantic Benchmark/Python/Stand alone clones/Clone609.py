def get_dir_size(root) :
	size = 0
	for path, dirs, files in os.walk(root) :
		for f in files :
			size += os.path.getsize(os.path.join(path, f))
	return size


def get_dir_size(path) :
	total_size = 0
	try :
		items = FindFilesW(path + r'\*')
	except pywintypes.error, ex :
		return total_size
	for item in items :
		total_size += item [5]
		if (item [0] & MASK == REQUIRED) :
			name = item [8]
			if name not in DIR_EXCLUDES :
				total_size += get_dir_size(path + '\\' + name)
	return total_size

