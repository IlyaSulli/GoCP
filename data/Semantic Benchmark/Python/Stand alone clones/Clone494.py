def treeToList(node, order = Order.INORDER) :
	if node is None :
		return []
	right = treeToList(node.right, order)
	down = treeToList(node.down, order)
	current = [node.data]
	if order == Order.PREORDER :
		return current + right + down
	if order == Order.INORDER :
		return right + current + down
	if order == Order.POSTORDER :
		return right + down + current


def treeToList(root, order = Order.INORDER) :
	ret = list()
	def inorder_traversal(node) :
		if node is not None :
			inorder_traversal(node.right)
			ret.append(node.data)
			inorder_traversal(node.down)
	def preorder_traversal(node) :
		if node is not None :
			ret.append(node.data)
			preorder_traversal(node.right)
			preorder_traversal(node.down)
	def postorder_traversal(node) :
		if node is not None :
			postorder_traversal(node.right)
			postorder_traversal(node.down)
			ret.append(node.data)
	if order == Order.PREORDER :
		preorder_traversal(node)
	elif order == Order.INORDER :
		inorder_traversal(node)
	else :
		postorder_traversal(node)
	return ret

