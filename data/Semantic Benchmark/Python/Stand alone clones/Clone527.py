def froze_it(cls) :
	cls.__frozen = False
	def frozensetattr(self, key, value) :
		if self.__frozen and not hasattr(self, key) :
			print ("Class {} is frozen. Cannot set {} = {}"
			.format(cls.__name__, key, value))
		else :
			object.__setattr__(self, key, value)
	def init_decorator(func) :
		@ wraps(func)
		def wrapper(self, * args, ** kwargs) :
			func(self, * args, ** kwargs)
			self.__frozen = True
		return wrapper
	cls.__setattr__ = frozensetattr
	cls.__init__ = init_decorator(cls.__init__)
	return cls


def froze_it(cls) :
	def frozensetattr(self, key, value) :
		if not hasattr(self, key) and inspect.stack() [1] [3] ! = "__init__" :
			print ("Class {} is frozen. Cannot set {} = {}"
			.format(cls.__name__, key, value))
		else :
			self.__dict__ [key] = value
	cls.__setattr__ = frozensetattr
	return cls

