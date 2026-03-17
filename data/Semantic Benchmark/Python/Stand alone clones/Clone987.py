def file_store(filename) :
	def store(items) :
		with open(filename, 'w') as output :
			results = []
			for item in items :
				write_result(item, result, output)
				result.append(item)
		return results
	return store


def file_store(filename, mode = 'w') :
	def store(items) :
		with open(filename, mode) as output :
			results = []
			for item in items :
				write_result(item, output)
				results.append(item)
		return results
	return store

