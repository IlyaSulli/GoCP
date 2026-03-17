def __init__(self, rect, pen, brush, tooltip = 'No tip here', parent = None) :
	super(GraphicsItem, self).__init__()
	self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
	self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
	self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable, True)
	self.setAcceptsHoverEvents(True)
	self.pen = pen
	pw = self.pen.widthF()
	self.brush = QtGui.QBrush(QtCore.Qt.blue)
	self.brush = brush
	self.setToolTip(tooltip)
	self.parent = parent
	self.rect = QtCore.QRectF(rect [0], rect [1], rect [2], rect [3])
	self.focusrect = QtCore.QRectF(rect [0] - pw / 2, rect [1] - pw / 2,
	rect [2] + pw, rect [3] + pw)


def __init__(self, parent = None) :
	super(MyMainWindow, self).__init__(parent)
	w = 1000
	h = 800
	self.scene = QtGui.QGraphicsScene(- w / 2, - h / 2, w, h)
	self.view = QtGui.QGraphicsView()
	self.view.setRenderHints(QtGui.QPainter.Antialiasing |
	QtGui.QPainter.HighQualityAntialiasing)
	self.view.setViewportUpdateMode(QtGui.QGraphicsView.FullViewportUpdate)
	self.view.setScene(self.scene)
	self.setCentralWidget(self.view)
	self.addGraphicsItem((0, 0, 250, 250), 8.0, (255, 0, 0), (0, 0, 255), 'My first item')
	self.addGraphicsItem((- 250, - 250, 300, 200), 4.0, (0, 0, 0), (255, 0, 100), 'My 2nd item')
	self.addGraphicsItem((200, - 200, 200, 200), 10.0, (0, 0, 255), (0, 255, 100), 'My 3rd item')

