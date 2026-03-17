def json_scan(json_obj, key) :
	result = None
	for element in json_obj :
		if str(element) == key :
			result = json_obj [element]
		else :
			if type(json_obj [element]) == DictType :
				result = json_scan(json_obj [element], key)
			elif type(json_obj [element]) == ListType :
				result = json_scan(element, key)
	return result


def json_scan(json_obj, key) :
	d = json.loads(json_obj)
	def _(dictobj, lookup) :
		if lookup in dictobj.keys() :
			return dictobj [lookup]
		else :
			for sub_dictobj in [d for d in dictobj.values() if type(d) == DictType] :
				result = _(sub_dictobj, lookup)
				if result :
					return result
			for listobject in [l for l in dictobj.values() if type(d) == list] :
				for sub_dictobj in [d for d in listobject if type(d) == DictType] :
					result = _(sub_dictobj, lookup)
					if result :
						return result
			return None
	return _(d, key)

