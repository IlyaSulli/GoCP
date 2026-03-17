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


def recurse(node, depth) :
	indent = "      " * depth
	if tree_.feature [node] ! = _tree.TREE_UNDEFINED :
		name = feature_name [node]
		threshold = tree_.threshold [node]
		codelines.append('{}if Xin["{}"] <= {}:\n'.format(indent, name, threshold))
		recurse(tree_.children_left [node], depth + 1)
		codelines.append('{}else:  # if Xin["{}"] > {}\n'.format(indent, name, threshold))
		recurse(tree_.children_right [node], depth + 1)
	else :
		codelines.append('{}mycat = {}\n'.format(indent, node))

