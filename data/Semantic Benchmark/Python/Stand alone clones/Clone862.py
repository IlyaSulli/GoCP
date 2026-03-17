def decorator2(method_to_decorate) :
	@ wraps(method_to_decorate)
	def wrapper2(self, request, * args, ** kwargs) :
		result = method_to_decorate(self, request, * args, ** kwargs)
		if isinstance(result, tuple) and result and result [0] == 'failure' :
			return result
		else :
			if decorator2_s_test_was_successful :
				return result
			else :
				return ('another failure', 'message')
	return wrapper2


def decorator2(f) :
	@ wraps(f)
	def wrapper(a) :
		if a > = 2 :
			return f(a)
		return 'failed in decorator 2'
	return wrapper

