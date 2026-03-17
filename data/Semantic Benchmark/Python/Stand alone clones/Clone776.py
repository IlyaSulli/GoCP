def removeRec(node, value) :
	if node.value == value :
		node.value = node.next.value
		node.next = node.next.next
		return True
	if node.next == None :
		return False
	if node.next.value == value :
		node.next = node.next.next
		return True
	return removeRec(node.next, value)


def removeRec(node, value) :
	if isinstance(node, EmptyNode) :
		print ("Cannot remove value from an empty list")
		return None
	elif node.data == value :
		return node.next
	else :
		rec_result = removeRec(node.next, value)
		if rec_result is None :
			return rec_result
		else :
			node.next = rec_result
			return node

