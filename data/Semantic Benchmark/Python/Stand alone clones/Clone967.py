def obj_get(self, request = None, ** kwargs) :
	try :
		info = Info.get(kwargs ['pk'])
	except ResourceNotFound :
		raise ObjectDoesNotExist('Sorry, no results on that page.')
	return info


def obj_get(self, request = None, ** kwargs) :
	try :
		base_object_list = self.get_object_list(request).filter(** kwargs)
		object_list = self.apply_authorization_limits(request, base_object_list)
		stringified_kwargs = ', '.join(["%s=%s" % (k, v) for k, v in kwargs.items()])
		if len(object_list) < = 0 :
			raise self._meta.object_class.DoesNotExist("Couldn't find an instance of '%s' which matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))
		elif len(object_list) > 1 :
			raise MultipleObjectsReturned("More than '%s' matched '%s'." % (self._meta.object_class.__name__, stringified_kwargs))
		return object_list [0]
	except ValueError :
		raise NotFound("Invalid resource lookup data provided (mismatched type).")

