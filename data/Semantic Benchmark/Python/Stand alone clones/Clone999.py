def __setattr__(self, name, value) :
	if name not in self._allowed_attrs :
		raise AttributeError(
		"Cannot set attribute {!r} on type {}".format(
		name, self.__class__.__name__))
	super(RestrictedAttributesObject, self).__setattr__(name, value)


def __setattr__(self, name, value) :
	if name == "_locked" :
		object.__setattr__(self, name, value)
		return
	if hasattr(self, "_locked") :
		if not self._locked or hasattr(self, name) :
			object.__setattr__(self, name, value)
		else :
			raise NameError("Not allowed to create new attribute {} in locked object".format(name))
	else :
		object.__setattr__(self, name, value)

