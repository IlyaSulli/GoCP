def compose(f, n) :
	def composed_f(x) :
		result = x
		for i in range(n) :
			result = f(result)
		return result
	return composed_f


def compose(g, m) :
	def composer(f, n, x) :
		if n == 0 : return x
		return compose(f, n - 1, f(x))
	return lambda x : composer(g, m, x)

