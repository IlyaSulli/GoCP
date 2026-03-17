def wordsInListsCounter(stringList) :
	elements = []
	for element in stringList :
		if len(element) < = threshold :
			elements.append(element)
	return elements


def wordsInListsCounter() :
	elements = listOfWords(list)
	if len(elements) ! = 0 :
		strLessThanThreshold = [x for x in elements if len(x) < = threshold]
		return strLessThanThreshold
	elif len(elements) == 0 :
		emptyString = "There are no words in this list"
		return emptyString
	else :
		error = "There is invalid information"
		return error

