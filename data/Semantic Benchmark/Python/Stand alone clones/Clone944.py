def timeout(func, args = (), kwargs = {}, timeout_duration = 1, default = None) :
	import signal
	class TimeoutError(Exception) :
		pass
	def handler(signum, frame) :
		raise TimeoutError()
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(timeout_duration)
	try :
		result = func(* args, ** kwargs)
	except TimeoutError as exc :
		result = default
	finally :
		signal.alarm(0)
	return result


def timeout(max_timeout) :
	def timeout_decorator(item) :
		@ functools.wraps(item)
		def func_wrapper(* args, ** kwargs) :
			pool = multiprocessing.pool.ThreadPool(processes = 1)
			async_result = pool.apply_async(item, args, kwargs)
			return async_result.get(max_timeout)
		return func_wrapper
	return timeout_decorator

