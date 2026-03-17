def __init__(self, parent) :
	wx.Panel.__init__(self, parent = parent)
	grid = gridlib.Grid(self)
	grid.CreateGrid(25, 12)
	sizer = wx.BoxSizer(wx.VERTICAL)
	sizer.Add(grid, 0, wx.EXPAND)
	self.SetSizer(sizer)


def __init__(self) :
	wx.Frame.__init__(self, None, wx.ID_ANY,
	"Panel Switcher Tutorial")
	self.panel_one = PanelOne(self)
	self.panel_two = PanelTwo(self)
	self.panel_two.Hide()
	self.sizer = wx.BoxSizer(wx.VERTICAL)
	self.sizer.Add(self.panel_one, 1, wx.EXPAND)
	self.sizer.Add(self.panel_two, 1, wx.EXPAND)
	self.SetSizer(self.sizer)
	menubar = wx.MenuBar()
	fileMenu = wx.Menu()
	switch_panels_menu_item = fileMenu.Append(wx.ID_ANY,
	"Switch Panels",
	"Some text")
	self.Bind(wx.EVT_MENU, self.onSwitchPanels,
	switch_panels_menu_item)
	menubar.Append(fileMenu, '&File')
	self.SetMenuBar(menubar)

