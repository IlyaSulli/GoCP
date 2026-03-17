def default(self, obj) :
	if isinstance(obj, datetime.datetime) :
		return obj.isoformat()
	elif isinstance(obj, datetime.date) :
		return obj.isoformat()
	elif isinstance(obj, datetime.timedelta) :
		return (datetime.datetime.min + obj).time().isoformat()
	else :
		return super(DateTimeEncoder, self).default(obj)


def default(self, obj) :
	if isinstance(obj, datetime.datetime) :
		ARGS = ('year', 'month', 'day', 'hour', 'minute',
		'second', 'microsecond')
		return {'__type__' : 'datetime.datetime',
		'args' : [getattr(obj, a) for a in ARGS]}
	elif isinstance(obj, datetime.date) :
		ARGS = ('year', 'month', 'day')
		return {'__type__' : 'datetime.date',
		'args' : [getattr(obj, a) for a in ARGS]}
	elif isinstance(obj, datetime.time) :
		ARGS = ('hour', 'minute', 'second', 'microsecond')
		return {'__type__' : 'datetime.time',
		'args' : [getattr(obj, a) for a in ARGS]}
	elif isinstance(obj, datetime.timedelta) :
		ARGS = ('days', 'seconds', 'microseconds')
		return {'__type__' : 'datetime.timedelta',
		'args' : [getattr(obj, a) for a in ARGS]}
	elif isinstance(obj, decimal.Decimal) :
		return {'__type__' : 'decimal.Decimal',
		'args' : [str(obj),]}
	else :
		return super().default(obj)

