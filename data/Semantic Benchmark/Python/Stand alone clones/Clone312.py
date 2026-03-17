def CalcSomething() :
	cache = {}
	def CalcSomething(a) :
		if cache.has_key(a) :
			return cache [a]
		cache [a] = ReallyCalc(a)
		return cache [a]
	return CalcSomething


def CalcSomething(a) :
	if cache.has_key(a) :
		return cache [a]
	cache [a] = ReallyCalc(a)
	return cache [a]

