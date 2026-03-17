def backwalk(predecessor_map, start, origin) :
	def deffered_output() :
		for i in output :
			yield i
	result, a = tee(deffered_output())
	b = imap(predecessor_map.get, a)
	output = takewhile(lambda x : x ! = origin, chain([start], b))
	return result


def backwalk(mymap, start, origin) :
	yield start
	current = mymap [start]
	while current ! = origin :
		yield current
		current = mymap [current]

