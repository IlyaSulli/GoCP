def recurse(node, depth, parent) :
	global k
	indent = "  " * depth
	if tree_.feature [node] ! = _tree.TREE_UNDEFINED :
		name = feature_name [node]
		threshold = tree_.threshold [node]
		s = "{} <= {} ".format(name, threshold, node)
		if node == 0 :
			pathto [node] = s
		else :
			pathto [node] = pathto [parent] + ' & ' + s
		recurse(tree_.children_left [node], depth + 1, node)
		s = "{} > {}".format(name, threshold)
		if node == 0 :
			pathto [node] = s
		else :
			pathto [node] = pathto [parent] + ' & ' + s
		recurse(tree_.children_right [node], depth + 1, node)
	else :
		k = k + 1
		print (k, ')', pathto [parent], tree_.value [node])


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

