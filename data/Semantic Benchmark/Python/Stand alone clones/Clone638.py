def mergeSort(L, compare = operator.lt) :
	if len(L) < 2 :
		return L [:]
	else :
		middle = int(len(L) / 2)
		left = mergeSort(L [: middle], compare)
		right = mergeSort(L [middle :], compare)
		return merge(left, right, compare)


def mergeSort(inputList) :
	listlen = len(inputList)
	if listlen == 1 :
		return inputList
	else :
		newlist = []
		if listlen % 2 == 0 :
			for i in range(listlen / 2) :
				newlist.append(mergeList(inputList [2 * i], inputList [2 * i + 1]))
		else :
			for i in range((listlen + 1) / 2) :
				if 2 * i + 1 < listlen :
					newlist.append(mergeList(inputList [2 * i], inputList [2 * i + 1]))
				else :
					newlist.append(inputList [2 * i])
		return mergeSort(newlist)

