def read_relationship(filename) :
	data = []
	with open(filename, 'rb') as f :
		reader = csv.reader(f, delimiter = '\t')
		next(reader, None)
		for row in reader :
			data.append([{
			'source' : {
			'id' : row [0],
			'start' : int(row [2]),
			'end' : int(row [3]),
			},
			'target' : {
			'id' : row [1],
			'start' : int(row [4]),
			'end' : int(row [5]),
			},
			}])
	with open('data/data.txt', 'w') as outfile :
		json.dump(data, outfile)


def read_relationship(filename) :
	data = []
	with open(filename) as f :
		f.next()
		for line in f :
			try :
				parts = line.rstrip().split('\t')
				query_name = parts [0]
				subject_name = parts [1]
				query_start = parts [2]
				query_end = parts [3]
				subject_start = parts [4]
				subject_end = parts [5]
				item = {
				'source' : {
				'id' : query_name,
				'start' : subject_name,
				'end' : query_start},
				'target' : {
				'id' : query_end,
				'start' : subject_start,
				'end' : subject_end}}
				data.append(item)
			except ValueError :
				pass
	with open('data/data.txt', 'w') as outfile :
		json.dump(data, outfile)

