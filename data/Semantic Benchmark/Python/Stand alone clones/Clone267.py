def recurse(node, depth) :
	indent = "  " * depth
	if tree_.feature [node] ! = _tree.TREE_UNDEFINED :
		name = feature_name [node]
		threshold = tree_.threshold [node]
		print "{}if {} <= {}:".format(indent, name, threshold)
		recurse(tree_.children_left [node], depth + 1)
		print "{}else:  # if {} > {}".format(indent, name, threshold)
		recurse(tree_.children_right [node], depth + 1)
	else :
		print "{}return {}".format(indent, tree_.value [node])


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

