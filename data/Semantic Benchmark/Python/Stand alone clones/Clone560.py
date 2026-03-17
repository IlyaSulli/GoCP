def access(obj, indexes) :
	def _get_item(subobj, index) :
		if isinstance(subobj, list) and index < len(subobj) :
			return subobj [index]
		return None
	return reduce(_get_item, indexes, obj)


def access(obj, indexes) :
	a = obj
	for i in indexes :
		try :
			a = a [i]
		except IndexError :
			return None
	return a

