def index(filename, lst) :
	with open(filename, 'r') as infile :
		lines = [line.split() for line in infile]
	word2linenumbers = defaultdict(list)
	for linenumber, line in enumerate(lines, 1) :
		for word in line :
			if word in lst :
				word2linenumbers [word].append(linenumber)
	return word2linenumbers


def index(filename, lst) :
	lst = set(lst)
	dic = {}
	with open(filename, 'r') as fobj :
		for lineno, line in enumerate(fobj, 1) :
			words = line.split()
			for word in words :
				if word in lst :
					dic.setdefault(word, []).append(lineno)
	return dic

