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


def __init__(self, guide, * args, ** kwargs) :
	self.guide = guide
	super(ChecklistForm, self).__init__(* args, ** kwargs)
	new_fields = OrderedDict()
	for tier, tasks in guide.tiers().items() :
		questions = [(t ['task'], t ['question']) for t in tasks if 'question' in t]
		new_fields [tier.lower()] = forms.MultipleChoiceField(
		label = tier,
		widget = forms.CheckboxSelectMultiple(),
		choices = questions,
		help_text = 'desired set of site features')
	new_fields ['name'] = self.fields ['name']
	new_fields ['email'] = self.fields ['email']
	new_fields ['website'] = self.fields ['website']
	self.fields = new_fields

