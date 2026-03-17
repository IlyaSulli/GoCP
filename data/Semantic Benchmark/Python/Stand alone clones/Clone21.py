def binary_search(a_list, item, start = 0, end = None) :
	end = end or len(a_list)
	if start == end :
		if a_list [start] == item :
			return start
		return False
	mid = start + ((end - start) / / 2)
	if a_list [mid] == item :
		return mid
	elif a_list [mid] > item :
		return binary_search(a_list, item, start = start, end = mid)
	elif a_list [mid] < item :
		return binary_search(a_list, item, start = mid + 1, end = end)
	else :
		return False


def binary_search(a_list, item) :
	if not a_list :
		return False
	mid = len(a_list) / / 2
	print "Middle is: {}".format(a_list [mid])
	print a_list
	print a_list, item
	pdb.set_trace()
	while len(a_list) > 0 :
		if a_list [mid] == item :
			return mid
		elif a_list [mid] > item :
			return binary_search(a_list [: mid], item)
		elif a_list [mid] < item :
			return binary_search(a_list [mid :], item) + mid
		else :
			return False

