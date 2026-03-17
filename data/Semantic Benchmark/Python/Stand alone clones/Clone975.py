def handleError(func) :
	errors = []
	def wrapper(arg1) :
		result = func(arg1)
		for err in findError(result) :
			errors.append(err)
		print errors
		return result
	return wrapper


def handleError(func) :
	def wrapper(arg1) :
		try :
			return func(arg1)
		except MyException as e :
			print "Error:", e.args
	return wrapper

