def create_lookup_list(data, domains) :
	domain_keys = defaultdict(lambda : defaultdict(count().next))
	out = []
	for row in data :
		out.append(tuple(domain_keys [dom] [val] for val, dom in zip(row, domains)))
	lookup_table = dict((k, sorted(d, key = d.get)) for k, d in domain_keys.items())
	return out, lookup_table


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

