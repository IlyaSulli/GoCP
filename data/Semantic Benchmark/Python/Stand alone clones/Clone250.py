def choices(self, cl) :
	yield {
	'selected' : self.value() == self.all_value,
	'query_string' : cl.get_query_string({self.parameter_name : self.all_value}, []),
	'display' : _('All'),
	}
	for lookup, title in self.lookup_choices :
		yield {
		'selected' : self.value() == force_text(lookup) or (self.value() == None and force_text(self.default_value()) == force_text(lookup)),
		'query_string' : cl.get_query_string({
		self.parameter_name : lookup,
		}, []),
		'display' : title,
		}


def choices(self, cl) :
	from django.utils.encoding import force_text
	for lookup, title in self.lookup_choices :
		yield {
		'selected' : self.value() == force_text(lookup),
		'query_string' : cl.get_query_string({
		self.parameter_name : lookup,
		}, []),
		'display' : title,
		}

