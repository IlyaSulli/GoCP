def all_pairs(lst) :
	if len(lst) < 2 :
		yield []
		return
	if len(lst) % 2 == 1 :
		for i in range(len(lst)) :
			for result in all_pairs(lst [: i] + lst [i + 1 :]) :
				yield result
	else :
		a = lst [0]
		for i in range(1, len(lst)) :
			pair = (a, lst [i])
			for rest in all_pairs(lst [1 : i] + lst [i + 1 :]) :
				yield [pair] + rest


def all_pairs(lst) :
	N = len(lst)
	choice_indices = itertools.product(* [
	xrange(k) for k in reversed(xrange(1, N, 2))])
	for choice in choice_indices :
		tmp = lst [:]
		result = []
		for index in choice :
			result.append((tmp.pop(0), tmp.pop(index)))
		yield result

