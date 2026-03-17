def __init__(self, method, args, uid, readycb, errorcb = None) :
	super(Request, self).__init__()
	self.setAutoDelete(True)
	self.cancelled = False
	self.method = method
	self.args = args
	self.uid = uid
	self.dataReady = readycb
	self.dataError = errorcb
	Request.INSTANCES.append(self)
	Request.FINISHED = []


def __init__(self) :
	super().__init__()
	self.initUI()
	self.worker = {}
	self.threadx = {}
	self.i = 0
	i = 0
	self.threadtest = QThread(self)
	self.idealthreadcount = self.threadtest.idealThreadCount()
	print ("This machine can handle {} threads optimally".format(self.idealthreadcount))
	while i < self.idealthreadcount :
		self.setupThread(i)
		i += 1
	i = 0
	while i < self.idealthreadcount :
		self.startThread(i)
		i += 1
	print ("Main Gui running in thread {}.".format(self.thread()))

