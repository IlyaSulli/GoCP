def curry(f) :
	@ wraps(f)
	def _(arg) :
		try :
			return f(arg)
		except TypeError :
			return curry(wraps(f)(partial(f, arg)))
	return _


def curry(x, argc = None) :
	if argc is None :
		argc = x.func_code.co_argcount
	def p(* a) :
		if len(a) == argc :
			return x(* a)
		def q(* b) :
			return x(* (a + b))
		return curry(q, argc - len(a))
	return p

