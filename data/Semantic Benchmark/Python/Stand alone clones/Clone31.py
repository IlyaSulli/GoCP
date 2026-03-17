def create_lookup_list(data, domains) :
	domain_keys = defaultdict(lambda : defaultdict(count().next))
	out = []
	for row in data :
		out.append(tuple(domain_keys [dom] [val] for val, dom in zip(row, domains)))
	lookup_table = dict((k, sorted(d, key = d.get)) for k, d in domain_keys.items())
	return out, lookup_table


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

