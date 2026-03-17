def __init__(self, a = None, b = None, ** kwargs) :
	self.relations = {
	"e" : {"req" : ["a", "b"], "func" : lambda a, b : a + b},
	"C" : {"req" : ["e", "a"], "func" : lambda e, a : e * 1 / (a * b)},
	"A" : {"req" : ["C", "e"], "func" : lambda e, C : cmplx_func_A(e, C)},
	"a" : {"req" : ["e", "b"], "func" : lambda e, b : e / b},
	"b" : {"req" : ["e", "a"], "func" : lambda e, a : e / a}}
	self.a = a
	self.b = b
	self.e = None
	self.C = None
	self.A = None
	if kwargs :
		for key in kwargs :
			setattr(self, key, kwargs [key])


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

