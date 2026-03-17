def __init__(self, parent = None) :
	super(UploadThread, self).__init__(parent)
	self.endNow = False
	self.fileName = None
	self.sig = MySigObj()
	self.fileNames = []
	self.uploaded = []


def __init__(self, parent = None) :
	super(ULoadWin, self).__init__(parent)
	self.upThread = UploadThread()
	self.sig = MySigObj()
	self.sig.tupSig.connect(self.upThread.setFileNames)
	self.upThread.sig.strSig.connect(self.txtMsgAppend)
	self.sig.tupSig.connect(self.upThread.setFileNames)
	self.layout = QtGui.QVBoxLayout()
	self.stButton = QtGui.QPushButton("Start")
	self.stButton.clicked.connect(self.uploadItems)
	self.stpButton = QtGui.QPushButton("Stop")
	self.stpButton.clicked.connect(self.killThread)
	self.testButton = QtGui.QPushButton("write txt\n not(?) blocked \nbelow")
	self.testButton.setMinimumHeight(28)
	self.testButton.clicked.connect(self.tstBlking)
	self.lbl = QtGui.QTextEdit()
	self.lbl.setMinimumHeight(325)
	self.lbl.setMinimumWidth(290)
	self.layout.addWidget(self.stButton)
	self.layout.addWidget(self.stpButton)
	self.layout.addWidget(self.testButton)
	self.layout.addWidget(self.lbl)
	self.setLayout(self.layout)
	self.l = ['a', 'list', 'of_files', 'we', 'will_pretend_to_upload', 'st', 'uploading']
	self.upThread.start()

