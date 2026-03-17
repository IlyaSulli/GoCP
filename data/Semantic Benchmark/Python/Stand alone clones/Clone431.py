def add_list_attributes(klass) :
	def new(cls, * args, ** kwargs) :
		result = super(cls, cls).__new__(cls)
		for attribute in klass.list_attributes :
			setattr(result, attribute, [])
		return result
	klass.__new__ = staticmethod(new)
	return klass


def add_list_attributes(klass) :
	old_init = klass.__init__
	def new_init(self, * args, ** kwargs) :
		for attribute in klass.list_attributes :
			setattr(self, attribute, [])
		old_init(self, * args, ** kwargs)
	klass.__init__ = new_init
	return klass

