def insert(self, btreeNode) :
	if self.data > btreeNode.data :
		if self.lChild == None :
			self.lChild = btreeNode
		else :
			self.lChild.insert(btreeNode)
	else :
		if self.rChild == None :
			self.rChild = btreeNode
		else :
			self.rChild.insert(btreeNode)


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

