def decorator(f) :
	@ wraps(f)
	def wrapper(* args, ** kwargs) :
		return "".join([f.__name__, ' ', start_val,
		f(* args, ** kwargs), end_val])
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

