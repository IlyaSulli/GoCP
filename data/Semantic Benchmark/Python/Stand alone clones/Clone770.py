def file_filter(name) :
	lst = []
	idtile = None
	for line in file(name, mode = "r") :
		element = line.split()
		if idtile is None :
			idtile = (int(element [0]), int(element [1]))
		if (int(element [0]), int(element [1])) == idtile :
			lst.append(element [2 :])
			dy, dx = int(element [0]), int(element [1])
		else :
			yield lst, dx, dy
			lst = []
			idtile = None


def file_filter(name, idtile) :
	lst = []
	id_str = "%d %d " % idtile
	with open(name) as f :
		for line in f :
			if line.startswith(id_str) :
				element = line.split()
				lst.append(element [2 :])
				dy, dx = int(element [0]), int(element [1])
	return (lst, dy, dx)

