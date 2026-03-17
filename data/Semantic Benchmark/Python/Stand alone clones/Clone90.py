def main() :
	@ clazzRef
	def BarOverride(self) :
		print "Hello, world! I'm a %s but this method is from class %s!" % (type(self), clazz)
		super(clazz, self).FooMethod()
	derived_type = type('Derived', (FooClass,), {'FooMethod' : BarOverride})
	instance = derived_type()
	instance.FooMethod()
	class derivedDerived(derived_type) :
		def FooMethod(self) :
			print 'I inherit from derived.'
			super(derivedDerived, self).FooMethod()
	instance = derivedDerived()
	instance.FooMethod()


def main() :
	derived_type = type('Derived', (FooClass,), {'FooMethod' : None})
	def BarOverride(self) :
		print 'Hello, world!'
	setattr(derived_type, 'FooMethod', BarOverride)
	instance = derived_type()

