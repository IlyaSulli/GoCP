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

