def arePermsEqualParity(perm0, perm1) :
	perm1 = list(perm1)
	perm1_map = dict((v, i) for i, v in enumerate(perm1))
	transCount = 0
	for loc, p0 in enumerate(perm0) :
		p1 = perm1 [loc]
		if p0 ! = p1 :
			sloc = perm1_map [p0]
			perm1 [loc], perm1 [sloc] = p0, p1
			perm1_map [p0], perm1_map [p1] = loc, sloc
			transCount += 1
	return (transCount % 2) == 0


def arePermsEqualParity(perm0, perm1) :
	transCount = 0
	for loc in range(len(perm0) - 1) :
		if perm0 [loc] ! = perm1 [loc] :
			sloc = perm1.index(perm0 [loc])
			perm1 [loc], perm1 [sloc] = perm1 [sloc], perm1 [loc]
			transCount += 1
	if (transCount % 2) == 0 :
		return True
	else :
		return False

