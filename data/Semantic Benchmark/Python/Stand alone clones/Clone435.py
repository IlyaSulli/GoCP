def __init__(self, * args, ** kw) :
	super(ModelForm, self).__init__(* args, ** kw)
	self.fields.keyOrder = [
	'super_user',
	'all_districts',
	'multi_district',
	'all_schools',
	'manage_users',
	'direct_login',
	'student_detail',
	'license']


def __init__(self) :
	self.fields = []
	for field_name in dir(self) :
		field = getattr(self, field_name)
		if isinstance(field, Field) :
			field.name = field_name
			self.fields.append(field)
	self.fields.sort(key = operator.attrgetter('count'))

