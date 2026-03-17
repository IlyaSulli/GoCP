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


def insert(self, data) :
	if self.root :
		return self.root._insert(data)
	else :
		self.root = Node(data)
		return True

