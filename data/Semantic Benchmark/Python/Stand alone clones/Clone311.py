def accept(func_or_mimetype = None) :
	mimetype = 'text/html'
	class Accept(object) :
		def __init__(self, func) :
			self.default_mimetype = mimetype
			self.accept_handlers = {mimetype : func}
			functools.update_wrapper(self, func)
		def __call__(self, * args, ** kwargs) :
			default = self.default_mimetype
			mimetypes = request.accept_mimetypes
			best = mimetypes.best_match(self.accept_handlers.keys(), default)
			if best ! = default and mimetypes [best] == mimetypes [default] :
				best = default
			return self.accept_handlers [best](* args, ** kwargs)
		def accept(self, mimetype) :
			def decorator(func) :
				self.accept_handlers [mimetype] = func
				return func
			return decorator
	if callable(func_or_mimetype) :
		return Accept(func_or_mimetype)
	if func_or_mimetype is not None :
		mimetype = func_or_mimetype
	return Accept


def accept(self, mimetype) :
	def decorator(func) :
		self.accept_handlers [mimetype] = func
		return func
	return decorator

