def create_lookup_list(data, domains) :
	domain_keys = defaultdict(lambda : defaultdict(count().next))
	out = []
	for row in data :
		out.append(tuple(domain_keys [dom] [val] for val, dom in zip(row, domains)))
	lookup_table = dict((k, sorted(d, key = d.get)) for k, d in domain_keys.items())
	return out, lookup_table


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

