def decorate(function) :
	def wrap_function(* args, ** kwargs) :
		str = 'Hello!'
		args.insert(1, str)
		return function(* args, ** kwargs)
	return wrap_function


def decorate(func) :
	def wrap_and_call(* args, ** kwargs) :
		if 'str' in inspect.getargspec(func).args :
			kwargs ['str'] = 'Hello!'
		return func(* args, ** kwargs)
	return wrap_and_call

