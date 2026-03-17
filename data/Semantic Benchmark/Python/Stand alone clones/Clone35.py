def create_lookup_list(messages, labels) :
	lookup = collections.defaultdict(set)
	for msg in messages :
		for l, v in zip(labels, msg) :
			lookup [l].add(v)
	for k, v in lookup.items() :
		lookup [k] = list(v)
	lookup_list = []
	for msg in messages :
		lookup_list.append([lookup [l].index(v) for l, v in zip(labels, msg)])
	return lookup_list, lookup


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

