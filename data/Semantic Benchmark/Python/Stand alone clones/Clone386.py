def decorator(file, f) :
	def df(* args, ** kwargs) :
		print 'redirecting to ', file
		return f(* args, ** kwargs)
	return df


def decorator(func = None, foo = 'spam') :
	if func is None :
		return partial(decorator, foo = foo)
	@ wraps(func)
	def wrapper(* args, ** kwargs) :
		pass
	return wrapper

