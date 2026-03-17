def curry(func) :
	def curried(* args, ** kwargs) :
		if len(args) + len(kwargs) > = func.__code__.co_argcount :
			return func(* args, ** kwargs)
		return (lambda * args2, ** kwargs2 :
		curried(* (args + args2), ** dict(kwargs, ** kwargs2)))
	return curried


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

