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


def insert(self, someNumber) :
	self.size = self.size + 1
	if self.root is None :
		self.root = Node(someNumber)
	else :
		self.insertWithNode(self.root, someNumber)

