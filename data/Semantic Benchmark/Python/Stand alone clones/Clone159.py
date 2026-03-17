def generateMenu(* args) :
	counter = 0
	for i in args :
		def recurse(l, counter) :
			for i in l :
				counter += 1
				if isinstance(i, (list, tuple)) :
					counter = recurse(i, counter)
				else :
					print ("{}. {}.".format(counter, i))
			return counter
		counter = recurse(i, counter)


def generateMenu(* args) :
	outer_counter = 1
	def recurse(l, inner_counter) :
		for i in l :
			if isinstance(i, (list, tuple)) :
				inner_counter = recurse(i, inner_counter)
			else :
				print ("{}. {}.".format(inner_counter, i))
				inner_counter += 1
		return inner_counter
	for i in args :
		outer_counter = recurse(i, outer_counter)

