def __init__(self, parent = None) :
	super().__init__(parent)
	self.log_txt = QtWidgets.QPlainTextEdit(self)
	self.log_txt.setReadOnly(True)
	layout = QtWidgets.QHBoxLayout(self)
	layout.addWidget(self.log_txt)
	self.setWindowTitle('Event Log')


def __init__(self) :
	super().__init__()
	widget = QtWidgets.QWidget()
	layout = QtWidgets.QHBoxLayout(widget)
	start_btn = QtWidgets.QPushButton('Start')
	start_btn.clicked.connect(self.start)
	layout.addWidget(start_btn)
	self.setCentralWidget(widget)
	self.log_dialog = LogDialog()
	self.running = False
	handler = LogHandler()
	handler.emitter.sigLog.connect(self.log_dialog.log_txt.appendPlainText)
	self.q = multiprocessing.Queue()
	self.ql = QueueListener(self.q, handler)
	self.ql.start()
	self.main_log = logging.getLogger('main')
	self.main_log.propagate = False
	self.main_log.setLevel(logging.INFO)
	self.main_log.addHandler(QueueHandler(self.q))
	self.pool = multiprocessing.Pool(1, worker_init, [self.q])

