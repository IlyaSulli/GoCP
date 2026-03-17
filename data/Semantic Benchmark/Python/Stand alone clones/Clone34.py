def create_lookup_list(messages, schema) :
	def mapped_rows(messages) :
		for row in messages :
			newRow = []
			for col, value in zip(schema, row) :
				if value not in lookups [col] :
					lookups [col].append(value)
				code = lookups [col].index(value)
				newRow.append(code)
			yield newRow
	lookups = defaultdict(list)
	return list(mapped_rows(messages)), dict(lookups)


def create_lookup_list(input_list, groups) :
	indices = dict((group, {}) for group in groups)
	output = []
	for row in input_list :
		newrow = []
		for group, element in zip(groups, row) :
			if element in indices [group] :
				index = indices [group] [element]
			else :
				index = indices [group] [element] = len(indices [group])
			newrow.append(index)
		output.append(newrow)
	lookup_dict = {}
	for group in indices :
		lookup_dict [group] = sorted(indices [group].keys(),
		lambda e1, e2 : indices [group] [e1] - indices [group] [e2])
	return output, lookup_dict

