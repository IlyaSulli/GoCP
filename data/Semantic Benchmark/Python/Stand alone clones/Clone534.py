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

