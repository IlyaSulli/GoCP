def unique() :
	uniq = defaultdict(list)
	for row in csv.reader(open('try.csv', 'r'), delimiter = ',') :
		uniq [(row [0], row [6])].append(row)
	for idx, row in uniq.iteritems() :
		yield row [0]


def unique() :
	rows = list(csv.reader(open('try.csv', 'r'), delimiter = ','))
	result = collections.OrderedDict()
	for r in rows :
		key = (r [1], r [6])
		if key not in result :
			result [key] = r
	return result.values()

