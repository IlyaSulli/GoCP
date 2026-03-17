def order_fields(* field_list) :
	def decorator(form) :
		original_init = form.__init__
		def init(self, * args, ** kwargs) :
			original_init(self, * args, ** kwargs)
			for field in field_list [: : - 1] :
				self.fields.insert(0, field, self.fields.pop(field))
		form.__init__ = init
		return form
	return decorator


def order_fields(form, field_list, throw_away = False) :
	if throw_away :
		form.fields.keyOrder = field_list
	else :
		for field in field_list [: : - 1] :
			form.fields.insert(0, field, form.fields.pop(field))

