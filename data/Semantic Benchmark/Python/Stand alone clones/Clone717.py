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

