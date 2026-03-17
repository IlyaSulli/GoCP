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


def __init__(self, parent, this_worker) :
	self.parent = parent
	self.this_worker = this_worker
	QtGui.QTabWidget.__init__(self, parent)
	self.treeWidget = QtGui.QTreeWidget(self)
	self.properties = QtGui.QTreeWidgetItem(self.treeWidget, ["Properties"])
	self.step = QtGui.QTreeWidgetItem(self.properties, ["Iteration #"])
	self.thread = QtCore.QThread();
	self.this_worker.moveToThread(self.thread);
	self.this_worker.update_signal.connect(self.update_GUI)
	self.this_worker.done_signal.connect(self.thread.quit)
	self.start_comp.connect(self.this_worker.start_computation)
	self.thread.start()

