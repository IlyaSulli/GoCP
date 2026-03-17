def __init__(self, ** kwargs) :
	available = set(kwargs)
	derivable = set()
	while True :
		for r in range(1, len(available) + 1) :
			for permutation in itertools.permutations(available, r) :
				if permutation in self.relationships :
					derivable.add(self.relationships [permutation])
		if derivable.issubset(available) :
			break
		else :
			available |= derivable
	underivable = set(self.relationships.values()) - available
	if len(underivable) > 0 :
		raise TypeError(
		"The following properties cannot be derived:\n\t{0}"
		.format(tuple(underivable)))
	self._value_dict = kwargs


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

