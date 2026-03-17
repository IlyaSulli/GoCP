def persistence(num) :
	def _persist(num, count = 0) :
		multi = 1
		while num :
			multi *= num % 10
			num /= 10
		if (multi > = 10) :
			return _persist(multi, count + 1)
		else :
			return count
	return _persist(num)


def persistence(num) :
	if len(str(num)) == 1 :
		return 0
	val = reduce(operator.mul, map(int, str(num)))
	return 1 + persistence(val)

