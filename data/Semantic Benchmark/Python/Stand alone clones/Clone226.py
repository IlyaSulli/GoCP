def insert(self, data) :
	if self.root :
		return self.root._insert(data)
	else :
		self.root = Node(data)
		return True


def insert(self, val) :
	if self.isEmpty() :
		self.val = val
	elif val < self.val :
		if self.left is None :
			self.left = BST(val)
		else :
			self.left.insert(val)
	else :
		if self.right is None :
			self.right = BST(val)
		else :
			self.right.insert(val)

