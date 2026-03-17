def binary_insert(root, node) :
	if root is None :
		root = node
	else :
		if root.data > node.data :
			if root.l_child is None :
				root.l_child = node
			else :
				binary_insert(root.l_child, node)
		else :
			if root.r_child is None :
				root.r_child = node
			else :
				binary_insert(root.r_child, node)


def binary_insert(root, node) :
	if root is None :
		return node
	if root.data > node.data :
		root.l_child = binary_insert(root.l_child, node)
	else :
		root.r_child = binary_insert(root.r_child, node)
	return root

