def convert(items, ID) :
	for key, value in items.items() :
		for keys, values in ID.items() :
			if keys == key :
				items [key] = values
	return items


def convert(items, ID) :
	result = {}
	for key, value in items.items() :
		if key in ID.keys() :
			result [ID [key]] = value
		else :
			result [key] = value
	items.clear()
	for key, value in result.items() :
		items [key] = value
	return items

