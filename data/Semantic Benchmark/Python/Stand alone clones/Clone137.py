def __new__(cls, name, bases, dct) :
	try :
		if Data in bases and "preprocess_data" in dct :
			f = dct ["preprocess_data"]
			@ wraps(f)
			def preprocess_data(self, * args, ** kwargs) :
				self.data = self.data.copy()
				return f(self, * args, ** kwargs)
			attrs = dct.copy()
			attrs ["preprocess_data"] = preprocess_data
	except NameError as e :
		attrs = dct
	return super(PreprocessMetaclass, cls).__new__(cls, name, bases, attrs)


def __new__(cls, name, bases, dictn) :
	fn = dictn.get('preprocess_data')
	if fn :
		if getattr(fn, '_original', False) is False :
			@ functools.wraps(fn)
			def wrapper(self, * args, ** kwargs) :
				self.data = self.data.copy()
				return fn(self, * args, ** kwargs)
			dictn ['preprocess_data'] = wrapper
	return type.__new__(cls, name, bases, dictn)

