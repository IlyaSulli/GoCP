def findError(result) :
	print result
	for k, v in result.iteritems() :
		error_nr = v % 2
		if error_nr == 0 :
			pass
		elif error_nr > 0 :
			yield MyException


def findError(func) :
	def wrapper(arg1) :
		errors = []
		result = func(arg1)
		for k, v in result.iteritems() :
			error_nr = v % 2
			if error_nr > 0 :
				errors.append((k, v, error_nr))
		if errors :
			raise MyException, errors
		return result
	return wrapper

