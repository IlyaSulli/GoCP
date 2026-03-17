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


def _add(self, val, node) :
	if (val < node.v) :
		if (node.l ! = None) :
			self._add(val, node.l)
		else :
			node.l = Node(val)
	else :
		if (node.r ! = None) :
			self._add(val, node.r)
		else :
			node.r = Node(val)

