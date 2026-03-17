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

