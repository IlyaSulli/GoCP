def recurse(left, right, threshold, features, node) :
	if (threshold [node] ! = - 2) :
		print "if ( " + features [node] + " <= " + str(threshold [node]) + " ) {"
		if left [node] ! = - 1 :
			recurse(left, right, threshold, features, left [node])
		print "} else {"
		if right [node] ! = - 1 :
			recurse(left, right, threshold, features, right [node])
		print "}"
	else :
		print "return " + str(value [node])


def recurse(left, right, child, lineage = None) :
	if lineage is None :
		lineage = [child]
	if child in left :
		parent = np.where(left == child) [0].item()
		split = 'l'
	else :
		parent = np.where(right == child) [0].item()
		split = 'r'
	lineage.append((parent, split, threshold [parent], features [parent]))
	if parent == 0 :
		lineage.reverse()
		return lineage
	else :
		return recurse(left, right, parent, lineage)

