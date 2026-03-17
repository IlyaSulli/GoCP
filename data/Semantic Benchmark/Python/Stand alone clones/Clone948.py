def insert(self, k) :
	t = TreeNode(k)
	parent = None
	node = self.root
	while node ! = None :
		parent = node
		if node.key > t.key :
			node = node.left
		else :
			node = node.right
	t.p = parent
	if parent == None :
		self.root = t
	elif t.key < parent.key :
		parent.left = t
	else :
		parent.right = t
	return t


def insert(self, val) :
	if self.val is not None :
		if val < self.val :
			if self.left is not None :
				self.left.insert(val)
			else :
				self.left = Tree(val)
		elif val > self.val :
			if self.right is not None :
				self.right.insert(val)
			else :
				self.right = Tree(val)
		else :
			return
	else :
		self.val = val
		print ("new node added")

