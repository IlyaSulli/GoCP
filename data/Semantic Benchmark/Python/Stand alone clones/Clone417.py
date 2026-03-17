def __init__(self, year = None, month = None,
day = None, weekday = None,
hour = None, minute = None,
second = None) :
	loc = locals()
	loc.pop("self")
	self.at = dict((k, v) for k, v in loc.iteritems() if v ! = None)


def __init__(self, action, min = allMatch, hour = allMatch,
day = allMatch, month = allMatch, dow = allMatch,
args = (), kwargs = {}) :
	self.mins = conv_to_set(min)
	self.hours = conv_to_set(hour)
	self.days = conv_to_set(day)
	self.months = conv_to_set(month)
	self.dow = conv_to_set(dow)
	self.action = action
	self.args = args
	self.kwargs = kwargs

