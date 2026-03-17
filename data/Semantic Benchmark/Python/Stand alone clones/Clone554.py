def chunks(iterable, n) :
	values = []
	for i, item in enumerate(iterable, 1) :
		values.append(item)
		if i % n == 0 :
			yield values
			values = []
	if values :
		yield values


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

