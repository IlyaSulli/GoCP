def _add(node, v) :
	new = [v, [], []]
	if node :
		left, right = node [1 :]
		if not left :
			left.extend(new)
		elif not right :
			right.extend(new)
		else :
			_add(left, v)
	else :
		node.extend(new)


def _add(self, node, value) :
	if value < = node.value :
		if node.left :
			self._add(node.left, value)
		else :
			node.left = Node(value)
	else :
		if node.right :
			self._add(node.right, value)
		else :
			node.right = Node(value)

