def chunks(iterable, n) :
	iterable = iter(iterable)
	while True :
		result = []
		for i in range(n) :
			try :
				a = next(iterable)
			except StopIteration :
				break
			else :
				result.append(a)
		if result :
			yield result
		else :
			break


def chunks(iterable, chunk_size) :
	i = 0;
	while i < len(iterable) :
		yield iterable [i : i + chunk_size]
		i += chunk_size

