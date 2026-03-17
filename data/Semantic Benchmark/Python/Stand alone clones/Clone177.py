def __init__(self, a = None, b = None, e = None, f = None) :
	if [a, b, e, f].count(None) > 2 :
		raise Exception('Not enough parameters to make an ellipse')
	self.a, self.b, self.e, self.f = a, b, e, f
	self.calculate_a()
	for parameter in 'b', 'e', 'f' :
		if self.__dict__ [parameter] is None :
			Ellipse.__dict__ ['calculate_' + parameter](self)


def __init__(self, ** kwargs) :
	super(MutexInit, self).__init__()
	for arg in kwargs :
		setattr(self, arg, kwargs.get(arg))
	self._arg_method_dict = {}
	for attr_name in dir(self) :
		attr = getattr(self, attr_name)
		if getattr(attr, "_isrequiredargsmethod", False) :
			self._arg_method_dict [attr.args] = attr
	provided_args = tuple(sorted(
	[arg for arg in kwargs if kwargs [arg] is not None]))
	sub_init = self._arg_method_dict.get(provided_args, None)
	if sub_init :
		sub_init(** kwargs)
	else :
		raise AttributeError('Insufficient arguments')

