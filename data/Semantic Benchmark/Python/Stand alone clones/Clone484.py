def underscore_to_camelcase(s) :
	def camelcase_words(words) :
		first_word_passed = False
		for word in words :
			if not word :
				yield "_"
				continue
			if first_word_passed :
				yield word.capitalize()
			else :
				yield word.lower()
			first_word_passed = True
	return ''.join(camelcase_words(s.split('_')))


def underscore_to_camelcase(value) :
	capitalized_words = [w.capitalize() if w else '_' for w in value.split('_')]
	for i, word in enumerate(capitalized_words) :
		if word ! = '_' :
			capitalized_words [i] = word.lower()
			break
	return "".join(capitalized_words)

