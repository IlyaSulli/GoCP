def salary_sort(thing) :
	def importantparts(thing) :
		unsortedlist = []
		for item in thing [1 :] :
			a = item.split(':')
			unsortedlist.append([a [1], a [0], int(a [8])])
		print unsortedlist
		sortedlist = sorted(unsortedlist, key = lambda item : item [2], reverse = True)
		return (sortedlist)
	return importantparts(thing)


def salary_sort(thing) :
	output = []
	for i in range(1, len(thing)) :
		a = thing [i].split(':')
		output.append([a [1], a [0], a [8]])
	sortedlist = sorted(output, key = lambda item : int(item [2]), reverse = True)
	return sortedlist

