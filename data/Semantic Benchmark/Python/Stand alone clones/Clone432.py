def __init__(self, parent) :
	mystyle = FNB.FNB_DROPDOWN_TABS_LIST | FNB.FNB_FF2 | FNB.FNB_SMART_TABS | FNB.FNB_X_ON_TAB
	super(MyFlatNotebook, self).__init__(parent, style = mystyle)
	self.textctrl = wx.TextCtrl(self, value = "edit me", style = wx.TE_MULTILINE)
	self.blue = wx.Panel(self)
	self.blue.SetBackgroundColour(wx.BLUE)
	self.AddPage(self.textctrl, "Text Editor")
	self.AddPage(self.blue, "Blue Panel")


def __init__(self, parent, id, title) :
	wx.Frame.__init__(self, parent, id, title)
	vbox = wx.BoxSizer(wx.VERTICAL)
	hbox = wx.BoxSizer(wx.HORIZONTAL)
	button = wx.Button(self, wx.ID_OK, "GoTo Blue Panel")
	self.Bind(wx.EVT_BUTTON, self.OnButton, button)
	hbox.Add(button, 0, wx.ALL, 5)
	self.nb = MyFlatNotebook(self)
	vbox.Add(hbox, 0, wx.EXPAND)
	vbox.Add(self.nb, 1, wx.EXPAND)
	self.SetSizer(vbox)

