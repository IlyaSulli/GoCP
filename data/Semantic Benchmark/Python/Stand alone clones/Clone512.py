def wrapper(f) :
	@ functools.wraps(f)
	def func(* args, ** kwargs) :
		if (time.time() - func.last_time) < interval :
			time.sleep(interval)
		result = f(* args, ** kwargs)
		func.last_time = time.time()
		return result
	func.last_time = time.time()
	return func


def wrapper(* args, ** kwargs) :
	time_diff = time.time() - last_time [0]
	if time_diff < 1 :
		print ("Too fast...")
		time.sleep(1 - time_diff)
		last_time [0] = time.time()
		return f(* args, ** kwargs)

