def __setattr__(self, name, value) :
	if name in ("_proxy", "collection") :
		object.__setattr__(self, name, value)
	else :
		proxied = self._proxy
		collection = self._collection
		old = getattr(proxied, name)
		setattr(proxy, name, value)
		collection.signal_change(proxied, name, old, value)


def __setattr__(self, name, value) :
	try :
		index = MyObject.indexes [name]
	except KeyError :
		index = weakref.WeakValueDictionary()
		MyObject.indexes [name] = index
	try :
		old_val = getattr(self, name)
		del index [old_val]
	except (KeyError, AttributeError) :
		pass
	object.__setattr__(self, name, value)
	index [value] = self

