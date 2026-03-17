def default(self, obj) :
	try :
		return super(DatetimeEncoder, obj).default(obj)
	except TypeError :
		return str(obj)


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

