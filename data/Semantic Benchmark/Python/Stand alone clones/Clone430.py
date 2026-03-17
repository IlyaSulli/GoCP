def get_fs_type(path) :
	partition = {}
	for part in psutil.disk_partitions() :
		partition [part.mountpoint] = (part.fstype, part.device)
	if path in partition :
		return partition [path]
	splitpath = path.split(os.sep)
	for i in xrange(len(splitpath), 0, - 1) :
		path = os.sep.join(splitpath [: i]) + os.sep
		if path in partition :
			return partition [path]
		path = os.sep.join(splitpath [: i])
		if path in partition :
			return partition [path]
	return ("unkown", "none")


def get_fs_type(mypath) :
	root_type = ""
	for part in psutil.disk_partitions() :
		if part.mountpoint == '/' :
			root_type = part.fstype
			continue
		if mypath.startswith(part.mountpoint) :
			return part.fstype
	return root_type

