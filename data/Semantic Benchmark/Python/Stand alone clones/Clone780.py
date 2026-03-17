def __new__(mcs, name, bases, dict) :
	def add_op(op) :
		if op in dict :
			return
		fn = lambda self, * args : self.__op__(op, args)
		fn.__name__ = op
		dict [op] = fn
	for op in mcs.__ops :
		add_op(op)
	return type.__new__(mcs, name, bases, dict)


def __new__(mcs, name, bases, dict) :
	def make_binary_op(op) :
		fn = lambda self, other : self.__op__(op, other)
		fn.__name__ = op
		return fn
	for opname in mcs.__binary_ops :
		for op in ('__%s__', '__r%s__') :
			op %= opname
			if op in dict :
				continue
			dict [op] = make_binary_op(op)
	def make_unary_op(op) :
		fn = lambda self : self.__op__(op, None)
		fn.__name__ = op
		return fn
	for opname in mcs.__unary_ops :
		op = '__%s__' % opname
		if op in dict :
			continue
		dict [op] = make_unary_op(op)
	return type.__new__(mcs, name, bases, dict)

