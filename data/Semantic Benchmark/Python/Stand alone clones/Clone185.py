def ensure_even(argnum) :
	def fdec(func) :
		def f(* args, ** kwargs) :
			assert (args [argnum] % 2 == 0)
			return func(* args, ** kwargs)
		return f
	return fdec


def ensure_even(* argvars) :
	def fdec(func) :
		def f(* args, ** kwargs) :
			for argvar in argvars :
				try :
					assert (not args [func.func_code.co_varnames.index(argvar)] % 2)
				except IndexError :
					assert (not kwargs [argvar] % 2)
			return func(* args, ** kwargs)
		return f
	return fdec

