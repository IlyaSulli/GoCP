def decorator(f) :
	args_names = inspect.getargspec(f) [0]
	def wrapper(* new_args, ** new_kwargs) :
		defaults = dict(defined_defaults, ** new_kwargs)
		if len(new_args) == 0 :
			return f(** defaults)
		elif len(new_args) == 1 and callable(new_args [0]) :
			return f(** defaults)(new_args [0])
		else :
			too_many_args = False
			if len(new_args) > len(args_names) :
				too_many_args = True
			else :
				for i in range(len(new_args)) :
					arg = new_args [i]
					arg_name = args_names [i]
					defaults [arg_name] = arg
			if len(defaults) > len(args_names) :
				too_many_args = True
			if not too_many_args :
				final_defaults = []
				for name in args_names :
					final_defaults.append(defaults [name])
				return f(* final_defaults)
			if too_many_args :
				raise TypeError("{0}() takes {1} argument(s) "
				"but {2} were given".
				format(f.__name__,
				len(args_names),
				len(defaults)))
	return wrapper


def decorator(method) :
	if callable(method_or_name) :
		method.gw_method = method.__name__
	else :
		method.gw_method = method_or_name
	@ wraps(method)
	def wrapper(* args, ** kwargs) :
		method(* args, ** kwargs)
	return wrapper

