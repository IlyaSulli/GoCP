def zipdir(path, ziph) :
	for root, dirs, files in os.walk(path) :
		for file in files :
			ziph.write(os.path.join(root, file))


def zipdir(path, ziph) :
	for root, dirs, files in os.walk(path) :
		if root.replace(path, '') == '' :
			prefix = ''
		else :
			prefix = root.replace(path, '') + '/'
			if (prefix [0] == '/') :
				prefix = prefix [1 :]
		for filename in files :
			actual_file_path = root + '/' + filename
			zipped_file_path = prefix + filename
			zipf.write(actual_file_path, zipped_file_path)

