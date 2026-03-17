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


def recurse(left, right, threshold, features, node, depth = 0) :
	offset = offset_unit * depth
	if (threshold [node] ! = - 2) :
		print (offset + "if ( " + features [node] + " <= " + str(threshold [node]) + " ) {")
		if left [node] ! = - 1 :
			recurse(left, right, threshold, features, left [node], depth + 1)
		print (offset + "} else {")
		if right [node] ! = - 1 :
			recurse(left, right, threshold, features, right [node], depth + 1)
		print (offset + "}")
	else :
		print (offset + "return " + str(value [node]))

