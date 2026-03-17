def __init__(self, parent = None) :
	super(MainWindow, self).__init__(parent)
	layout = QtWidgets.QHBoxLayout(self)
	menu_btn = QtWidgets.QPushButton()
	open_list_btn = QtWidgets.QPushButton('open list')
	layout.addWidget(menu_btn)
	layout.addWidget(open_list_btn)
	menu = QtWidgets.QMenu()
	menu_btn.setMenu(menu)
	self.menu_manager = MenuManager("menu_items", "Menu")
	menu.addMenu(self.menu_manager.menu)
	self.menu_manager.menu.triggered.connect(self.menu_clicked)
	open_list_btn.clicked.connect(self.menu_manager.show)


def __init__(self, key, menuname, parent = None) :
	super(MenuManager, self).__init__(parent)
	self.settings = QtCore.QSettings('test_org', 'my_app')
	self.key = key
	self.layout = QtWidgets.QVBoxLayout(self)
	self.listWidget = QtWidgets.QListWidget()
	self.remove_btn = QtWidgets.QPushButton('Remove')
	self.layout.addWidget(self.listWidget)
	self.layout.addWidget(self.remove_btn)
	self.remove_btn.clicked.connect(self.remove_items)
	self.menu = QtWidgets.QMenu(menuname)
	load_items = self.settings.value(self.key, [])
	for name, itemdata in load_items.items() :
		action = QtWidgets.QAction(name, self.menu)
		action.setData(itemdata)
		self.menu.addAction(action)
		item = QtWidgets.QListWidgetItem(name)
		item.setData(QtCore.Qt.UserRole, action)
		self.listWidget.addItem(item)

