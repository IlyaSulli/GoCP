def __new__(meta, name, bases, attrs) :
	nt = namedtuple(name, attrs.pop('fields'))
	struct = attrs.pop('struct')
	def factory(record) :
		return nt._make(unpack(struct, record))
	return factory


def __new__(cls, clsname, bases, dct) :
	nt = collections.namedtuple(clsname, dct ['fields'])
	def new(cls, record) :
		return super(cls, cls).__new__(cls, * struct.unpack(dct ['struct'], record))
	dct.update(__new__ = new)
	return super(MetaStruct, cls).__new__(cls, clsname, (nt,), dct)

