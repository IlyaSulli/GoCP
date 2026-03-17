def __init__(self, input, output) :
	try :
		self.input = open(input, 'r')
		self.output = open(output, 'w')
	except BaseException as exc :
		self.__exit___(type(exc), exc, exc.__traceback__)
		raise


def __init__(self, resources, acquire_resource, release_resource,
check_resource_ok = None) :
	super().__init__()
	self.acquire_resource = acquire_resource
	self.release_resource = release_resource
	if check_resource_ok is None :
		def check_resource_ok(resource) :
			return True
	self.check_resource_ok = check_resource_ok
	self.resources = resources
	self.wrappers = []

