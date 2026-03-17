def decorator_factory(value) :
	def msg_decorator(f) :
		def inner_dec(* args, ** kwargs) :
			g = f.__globals__
			sentinel = object()
			oldvalue = g.get('var', sentinel)
			g ['var'] = value
			try :
				res = f(* args, ** kwargs)
			finally :
				if oldvalue is sentinel :
					del g ['var']
				else :
					g ['var'] = oldvalue
			return res
		return inner_dec
	return msg_decorator


def decorator_factory(value) :
	def msg_decorator(f) :
		def inner_dec(* args, ** kwargs) :
			res = f(value, * args, ** kwargs)
			return res
		inner_dec.__name__ = f.__name__
		inner_dec.__doc__ = f.__doc__
		return inner_dec
	return msg_decorator

