def __init__(self, verbosity = 1) :
	TestResult.__init__(self)
	self.stdout0 = None
	self.stderr0 = None
	self.success_count = 0
	self.failure_count = 0
	self.error_count = 0
	self.verbosity = verbosity
	self.result = []


def __init__(self, stream = sys.stdout, verbosity = 1, title = None, description = None) :
	self.stream = stream
	self.verbosity = verbosity
	if title is None :
		self.title = self.DEFAULT_TITLE
	else :
		self.title = title
	if description is None :
		self.description = self.DEFAULT_DESCRIPTION
	else :
		self.description = description
	self.startTime = datetime.datetime.now()

