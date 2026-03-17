def convert(X, Y) :
	new_dict = {}
	for x_key, x_value in X.items() :
		for y_key, y_value in Y.items() :
			if x_key == y_key :
				new_dict [y_value] = x_value
	return new_dict


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

