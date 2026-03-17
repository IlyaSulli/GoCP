def wrapped_decorator(* args) :
	if len(args) == 1 and callable(args [0]) :
		return fn(args [0])
	else :
		def real_decorator(decoratee) :
			return fn(decoratee, * args)
		return real_decorator


def wrapped_decorator(* args, ** kwargs) :
	is_bound_method = hasattr(args [0], fn.__name__) if args else False
	if is_bound_method :
		klass = args [0]
		args = args [1 :]
	if len(args) == 1 and len(kwargs) == 0 and callable(args [0]) :
		if is_bound_method :
			return fn(klass, args [0])
		else :
			return fn(args [0])
	else :
		def real_decorator(decoratee) :
			if is_bound_method :
				return fn(klass, decoratee, * args, ** kwargs)
			else :
				return fn(decoratee, * args, ** kwargs)
		return real_decorator

