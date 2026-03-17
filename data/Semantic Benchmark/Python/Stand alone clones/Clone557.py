def match_class(target) :
	target = target.split()
	def do_match(tag) :
		try :
			classes = dict(tag.attrs) ["class"]
		except KeyError :
			classes = ""
		classes = classes.split()
		return all(c in classes for c in target)
	return do_match


def match_class(target) :
	def do_match(tag) :
		classes = tag.get('class', [])
		return all(c in classes for c in target)
	return do_match

