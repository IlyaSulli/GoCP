def __init__(self, parent = None) :
	QtGui.QMainWindow.__init__(self)
	self.tab_list = []
	self.setTabShape(QtGui.QTabWidget.Rounded)
	self.centralwidget = QtGui.QWidget(self)
	self.top_level_layout = QtGui.QGridLayout(self.centralwidget)
	self.tabWidget = QtGui.QTabWidget(self.centralwidget)
	self.top_level_layout.addWidget(self.tabWidget, 1, 0, 25, 25)
	process_button = QtGui.QPushButton("Process")
	self.top_level_layout.addWidget(process_button, 0, 1)
	QtCore.QObject.connect(process_button, QtCore.SIGNAL("clicked()"), self.process)
	self.setCentralWidget(self.centralwidget)
	self.centralwidget.setLayout(self.top_level_layout)
	for i in range(0, 10) :
		name = 'tab' + str(i)
		self.tab_list.append(Tab(self.tabWidget, Worker(name)))
		self.tabWidget.addTab(self.tab_list [- 1], name)


def __init__(self) :
	QMainWindow.__init__(self)
	self.toolBar = self.addToolBar("Toolbar")
	self.toolBar.addAction(QAction('Add Task', self, triggered = self.addTask))
	self.table = QTableWidget()
	self.table.verticalHeader().hide()
	self.table.setColumnCount(2)
	self.setCentralWidget(self.table)
	self.queue = multiprocessing.Queue()
	self.pool = multiprocessing.Pool(processes = 4, initializer = pool_init, initargs = (self.queue,))
	self.timer = QTimer()
	self.timer.timeout.connect(self.updateProgress)
	self.timer.start(2000)

