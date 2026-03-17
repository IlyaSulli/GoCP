def __getattr__(self, key) :
	try :
		return self [key]
	except KeyError :
		raise AttributeError(key)


def __getattr__(self, name) :
	try :
		value = self._data [name]
	except KeyError :
		if not super(DictWrap, self).__getattribute__('__create') :
			raise
		value = {}
		self._data [name] = value
	if hasattr(value, 'items') :
		create = super(DictWrap, self).__getattribute__('__create')
		return DictWrap(value, create)
	return value

