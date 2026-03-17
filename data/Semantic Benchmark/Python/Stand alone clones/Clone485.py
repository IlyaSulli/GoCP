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
	def camelcase() :
		yield str.lower
		while True :
			yield str.capitalize
	c = camelcase()
	return "".join(c.next()(x) if x else '_' for x in value.split("_"))

