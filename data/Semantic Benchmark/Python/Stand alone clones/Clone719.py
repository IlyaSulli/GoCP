def index(filename, lst) :
	infile = open('raven.txt', 'r')
	lines = infile.readlines()
	words = []
	dic = {}
	for line in lines :
		line_words = line.split(' ')
		words.append(line_words)
	for i in range(len(words)) :
		for j in range(len(words [i])) :
			if words [i] [j] in lst :
				if words [i] [j] not in dic.keys() :
					dic [words [i] [j]] = set()
				dic [words [i] [j]].add(i + 1)
	return dic


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

