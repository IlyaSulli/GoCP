def fires() :
	def beforeDecorator(f, event) :
		@ wraps(f)
		def wrapped(* args, ** kargs) :
			event.fire(* args, ** kargs)
			return f(* args, ** kargs)
		return wrapped
	def afterDecorator(f, event) :
		@ wraps(f)
		def wrapped(* args, ** kargs) :
			try :
				result = f(* args, ** kargs)
			finally :
				event.fire(* args, ** kargs)
			return result
		return wrapped
	def closure(event, after = False) :
		def decorator(function) :
			if after :
				return afterDecorator(function, event)
			else :
				return beforeDecorator(function, event)
		return decorator
	return closure


def fires(event, before = True) :
	if before :
		def decorator(f) :
			@ wraps(f)
			def wrapped(* args, ** kargs) :
				event.fire(* args, ** kargs)
				return f(* args, ** kargs)
			return wrapped
	else :
		def decorator(f) :
			@ wraps(f)
			def wrapped(* args, ** kargs) :
				result = f(* args, ** kargs)
				event.fire(* args, ** kargs)
				return result
			return wrapped
	return decorator

