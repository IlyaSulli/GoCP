def __init__(self, a) :
	self.a = a
	self.li = []
	def mydecorator(f) :
		self.li.append(f)
		return f
	@ mydecorator
	def afunction(self) :
		print ('a')
	self.afunction = new.instancemethod(afunction, self, Foo)


def __init__(self, a) :
	self.a = a
	self.li = [self.afunction]
	def afunction(self) :
		pass

