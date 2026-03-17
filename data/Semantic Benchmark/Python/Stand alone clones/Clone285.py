def is_sequence_same(list_a, list_b) :
	if list_a and list_a [0] in list_b :
		first = list_b.index(list_a [0])
	else :
		return False
	return list_a == (list_b [first :] + list_b [: first])


def is_sequence_same(l1, l2) :
	if l1 == l2 :
		return True
	if set(l1) ! = set(l2) or len(l1) ! = len(l2) :
		return False
	d2 = deque(l2)
	for i in range(len(l2)) :
		if l1 == list(d2) :
			return True
		d2.rotate()
	return False

