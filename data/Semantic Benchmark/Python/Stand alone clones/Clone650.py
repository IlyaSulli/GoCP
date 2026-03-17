def __init__(self) :
	super().__init__()
	self.label = QLabel("0")
	self.obj = worker.Worker()
	self.thread = QThread()
	self.obj.intReady.connect(self.onIntReady)
	self.obj.moveToThread(self.thread)
	self.obj.finished.connect(self.thread.quit)
	self.thread.started.connect(self.obj.procCounter)
	self.thread.start()
	self.initUI()


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

