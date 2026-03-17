def default(self, obj) :
	if isinstance(obj, datetime.datetime) :
		encoded_object = list(obj.timetuple()) [0 : 6]
	else :
		encoded_object = json.JSONEncoder.default(self, obj)
	return encoded_object


def default(obj) :
	import calendar, datetime
	if isinstance(obj, datetime.datetime) :
		if obj.utcoffset() is not None :
			obj = obj - obj.utcoffset()
		millis = int(
		calendar.timegm(obj.timetuple()) * 1000 +
		obj.microsecond / 1000)
		return millis
	raise TypeError('Not sure how to serialize %s' % (obj,))

