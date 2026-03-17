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

