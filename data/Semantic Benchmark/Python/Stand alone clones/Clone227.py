def insert(self, someNumber) :
	self.size = self.size + 1
	if self.root is None :
		self.root = Node(someNumber)
	else :
		self.insertWithNode(self.root, someNumber)


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

