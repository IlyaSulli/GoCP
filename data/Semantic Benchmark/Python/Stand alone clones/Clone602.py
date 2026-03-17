def __call__(self, new) :
	params = self.immutable_params
	def __set_if_unset__(self, name, value) :
		if name in self.__dict__ :
			raise Exception("Attribute %s has already been set" % name)
		if not name in params :
			raise Exception("Cannot create atribute %s" % name)
		self.__dict__ [name] = value;
	def __new__(cls, * args, ** kws) :
		cls.__setattr__ = __set_if_unset__
		return super(cls.__class__, cls).__new__(cls, * args, ** kws)
	return __new__


def __call__(cls, * args, ** kwargs) :
	self = cls.__new__(cls)
	set_mutability(self, True)
	self.__init__(* args, ** kwargs)
	set_mutability(self, False)
	return self

