def subset(l) :
	if not l :
		return [[]]
	rest = subset(l [1 :])
	return rest + [[l [0]] + s for s in rest]


def subset(set) :
	if len(set) == 0 :
		return [set]
	elif len(set) == 1 :
		return [set] + [[]]
	else :
		short = subset(set [1 :])
		alist = []
		for item in short :
			blist = [set [0]]
			blist += item
			alist.append(blist)
		return short + alist

