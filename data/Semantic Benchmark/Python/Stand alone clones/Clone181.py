def __eq__(self, other) :
	if not isinstance(other, FrozenDict) :
		return dict(self.iteritems()) == other
	if len(self) ! = len(other) :
		return False
	for key, value in self.iteritems() :
		try :
			if value ! = other [key] :
				return False
		except KeyError :
			return False
	return True


def __eq__(self, other) :
	if self is other :
		return True
	if isinstance(self, type(other)) :
		return self._data == other._data
	else :
		return NotImplemented

