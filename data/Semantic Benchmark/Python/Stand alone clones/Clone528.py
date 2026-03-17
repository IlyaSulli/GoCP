def __new__(cls, name, bases, dct) :
	def generate_test_method() :
		def test_method(self) :
			pass
		return test_method
	dct ['test_method'] = generate_test_method()
	return type.__new__(cls, name, bases, dct)


def __new__(cls, name, bases, attrs) :
	funcs = [t for t in dir(UnderTest) if t [0] == 'f']
	def doTest(t) :
		def f(slf) :
			ut = UnderTest()
			getattr(ut, t)(3)
		return f
	for f in funcs :
		attrs ['test_gen_' + f] = doTest(f)
	return type.__new__(cls, name, bases, attrs)

