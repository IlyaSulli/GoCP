def __init__(self, obj) :
	if self.__wraps__ is None :
		raise TypeError("base class Wrapper may not be instantiated")
	elif isinstance(obj, self.__wraps__) :
		self._obj = obj
	else :
		raise ValueError("wrapped object must be of %s" % self.__wraps__)


def __init__(cls, name, bases, dct) :
	def make_proxy(name) :
		def proxy(self, * args) :
			return getattr(self._obj, name)
		return proxy
	type.__init__(cls, name, bases, dct)
	if cls.__wraps__ :
		ignore = set("__%s__" % n for n in cls.__ignore__.split())
		for name in dir(cls.__wraps__) :
			if name.startswith("__") :
				if name not in ignore and name not in dct :
					setattr(cls, name, property(make_proxy(name)))

