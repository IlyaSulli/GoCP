def arity(func) :
	pfunc = func
	i = 0
	while True :
		try :
			pfunc()
		except TypeError :
			pfunc = partial(pfunc, '')
			i += 1
		else :
			return i


def arity(method) :
	def _arity() :
		return method.func_code.co_argcount - 1
	method.arity = _arity
	return method

