def validator(test) :
	def wrap(func) :
		def wrapped(* args, ** kwargs) :
			result = func(* args, ** kwargs)
			if test(result) :
				return result
			return None
		return wrapped
	return wrap


def validator(validate_func) :
	func = partial(patched, validate_func, input)
	patch = unittest.mock.patch('builtins.input', func)
	patch.start()
	try :
		yield
	finally :
		patch.stop()

