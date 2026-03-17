def __init__(self, * args, ** kwargs) :
	super(MainFrame, self).__init__(None, * args, ** kwargs)
	self.Title = 'Basic wxPython module'
	self.SetMenuBar(MenuBar(self))
	self.ToolBar = MainToolbar(self)
	self.status_bar = StatusBar(self).status_bar
	self.Bind(wx.EVT_CLOSE, self.on_quit_click)
	panel = MainPanel(self)
	sizer = wx.BoxSizer()
	sizer.Add(panel)
	self.SetSizerAndFit(sizer)
	self.Centre()
	self.Show()


def __init__(self, parent, * args, ** kwargs) :
	super(MenuBar, self).__init__(* args, ** kwargs)
	file_menu = wx.Menu()
	self.Append(file_menu, '&File')
	quit_menu_item = wx.MenuItem(file_menu, wx.ID_EXIT)
	parent.Bind(wx.EVT_MENU, parent.on_quit_click, id = wx.ID_EXIT)
	file_menu.Append(quit_menu_item)

