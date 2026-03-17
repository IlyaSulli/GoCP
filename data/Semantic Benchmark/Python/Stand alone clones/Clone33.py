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

