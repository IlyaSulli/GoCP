def __init__(self, parent = None) :
	super(TranslucentWidget, self).__init__(parent)
	self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
	self.fillColor = QtGui.QColor(30, 30, 30, 120)
	self.penColor = QtGui.QColor("#333333")
	self.popup_fillColor = QtGui.QColor(240, 240, 240, 255)
	self.popup_penColor = QtGui.QColor(200, 200, 200, 255)
	self.close_btn = QtWidgets.QPushButton(self)
	self.close_btn.setText("x")
	font = QtGui.QFont()
	font.setPixelSize(18)
	font.setBold(True)
	self.close_btn.setFont(font)
	self.close_btn.setStyleSheet("background-color: rgb(0, 0, 0, 0)")
	self.close_btn.setFixedSize(30, 30)
	self.close_btn.clicked.connect(self._onclose)
	self.SIGNALS = TranslucentWidgetSignals()


def __init__(self, parent = None) :
	super(ParentWidget, self).__init__(parent)
	self._popup = QtWidgets.QPushButton("Gimme Popup!!!")
	self._popup.setFixedSize(150, 40)
	self._popup.clicked.connect(self._onpopup)
	self._other1 = QtWidgets.QPushButton("A button")
	self._other2 = QtWidgets.QPushButton("A button")
	self._other3 = QtWidgets.QPushButton("A button")
	self._other4 = QtWidgets.QPushButton("A button")
	hbox = QtWidgets.QHBoxLayout()
	hbox.addWidget(self._popup)
	hbox.addWidget(self._other1)
	hbox.addWidget(self._other2)
	hbox.addWidget(self._other3)
	hbox.addWidget(self._other4)
	self.setLayout(hbox)
	self._popframe = None
	self._popflag = False

