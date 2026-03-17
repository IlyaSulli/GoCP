def curry(func) :
	def curried(* args, ** kwargs) :
		if len(args) + len(kwargs) > = func.__code__.co_argcount :
			return func(* args, ** kwargs)
		return (lambda * args2, ** kwargs2 :
		curried(* (args + args2), ** dict(kwargs, ** kwargs2)))
	return curried


def curry(f) :
	@ wraps(f)
	def _(arg) :
		try :
			return f(arg)
		except TypeError :
			return curry(wraps(f)(partial(f, arg)))
	return _

