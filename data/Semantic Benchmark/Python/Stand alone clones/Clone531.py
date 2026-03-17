def __init__(self, some_var) :
	QtCore.QObject.__init__(self, parent = None)
	self.some_var = some_var
	self.queue = mp.Queue()
	self.process = mp.Process(
	target = workermodule.some_complex_processing,
	args = (self.queue,))


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

