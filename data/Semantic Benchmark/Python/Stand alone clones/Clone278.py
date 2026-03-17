def scan(words) :
	result = []
	for word in words.split() :
		found_category = 'error'
		for category, category_lexicon in _LEXICON.items() :
			if word in category_lexicon :
				found_category = category
				break
		result.append((found_category, word))
	return result


def scan(thewords) :
	thewords = thewords.split()
	sentence = []
	for i in thewords :
		if i in directions :
			sentence.append(('direction', i))
		elif i in verbs :
			sentence.append(('verb', i))
		elif i in stops :
			sentence.append(('stop', i))
		elif i in nouns :
			sentence.append(('noun', i))
		elif i.isdigit() :
			sentence.append(('number', convert_number(i)))
		else :
			sentence.append(('error', i))
	return sentence

