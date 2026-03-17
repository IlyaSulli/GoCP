def scan(self, input) :
	self.result = []
	for word in input.split() :
		try :
			self.result.append(('number', int(word)))
		except ValueError :
			for category, item in self.mapping.items() :
				if word.lower() in item :
					found_category = category
					break
				else :
					found_category = 'error'
			self.result.append((found_category, word))
	return self.result


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

