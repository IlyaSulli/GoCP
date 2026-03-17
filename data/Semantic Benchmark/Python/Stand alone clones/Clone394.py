def __init__(self, parent) :
	super(MyInterpreter, self).__init__(parent)
	hBox = QHBoxLayout()
	self.setLayout(hBox)
	self.textEdit = PyInterp(self)
	self.textEdit.initInterpreter(locals())
	self.resize(850, 400)
	hBox.addWidget(self.textEdit)
	hBox.setMargin(0)
	hBox.setSpacing(0)


def __init__(self, parent) :
	super(PyInterp, self).__init__(parent)
	sys.stdout = self
	sys.stderr = self
	self.refreshMarker = False
	self.multiLine = False
	self.command = ''
	self.printBanner()
	self.marker()
	self.history = []
	self.historyIndex = - 1
	self.interpreterLocals = {}
	self.setFont(QFont('Courier', 10))
	self.initInterpreter(locals())
	from rlcompleter2 import Completer
	self.completer = Completer()

