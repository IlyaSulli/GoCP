def mergeSort(alist) :
	print ("Splitting ", alist)
	if len(alist) > 1 :
		mid = len(alist) / / 2
		lefthalf = alist [: mid]
		righthalf = alist [mid :]
		mergeSort(lefthalf)
		mergeSort(righthalf)
		i = 0
		j = 0
		k = 0
		while i < len(lefthalf) and j < len(righthalf) :
			if lefthalf [i] < righthalf [j] :
				alist [k] = lefthalf [i]
				i = i + 1
			else :
				alist [k] = righthalf [j]
				j = j + 1
			k = k + 1
		while i < len(lefthalf) :
			alist [k] = lefthalf [i]
			i = i + 1
			k = k + 1
		while j < len(righthalf) :
			alist [k] = righthalf [j]
			j = j + 1
			k = k + 1
	print ("Merging ", alist)


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

