def scan(sentence) :
	tuples = []
	words = sentence.split()
	for word in words :
		try :
			tuples.append((lexicons [word], word))
		except KeyError :
			if word.isdigit() :
				tuples.append(('number', int(word)))
			else :
				tuples.append(('error', word))
	return tuples


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

