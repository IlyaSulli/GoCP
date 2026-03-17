def __init__(self) :
	wx.Frame.__init__(self, None, wx.ID_ANY,
	"Text Validation Tutorial")
	panel = wx.Panel(self)
	textOne = wx.TextCtrl(panel, validator = CharValidator('no-alpha'))
	textTwo = wx.TextCtrl(panel, validator = CharValidator('no-digit'))
	sizer = wx.BoxSizer(wx.VERTICAL)
	sizer.Add(textOne, 0, wx.ALL, 5)
	sizer.Add(textTwo, 0, wx.ALL, 5)
	panel.SetSizer(sizer)


def __init__(self, parent) :
	wx.Dialog.__init__(self, parent, - 1, "Validated Dialog")
	self.SetAutoLayout(True)
	VSPACE = 10
	fgs = wx.FlexGridSizer(0, 2)
	fgs.Add((1, 1));
	fgs.Add(wx.StaticText(self, - 1,
	"These controls must have text entered into them.  Each\n"
	"one has a validator that is checked when the Okay\n"
	"button is clicked."))
	fgs.Add((1, VSPACE)); fgs.Add((1, VSPACE))
	label = wx.StaticText(self, - 1, "First: ")
	fgs.Add(label, 0, wx.ALIGN_RIGHT | wx.CENTER)
	fgs.Add(wx.TextCtrl(self, - 1, "", validator = TextObjectValidator()))
	fgs.Add((1, VSPACE)); fgs.Add((1, VSPACE))
	label = wx.StaticText(self, - 1, "Second: ")
	fgs.Add(label, 0, wx.ALIGN_RIGHT | wx.CENTER)
	fgs.Add(wx.TextCtrl(self, - 1, "", validator = TextObjectValidator()))
	buttons = wx.StdDialogButtonSizer()
	b = wx.Button(self, wx.ID_OK, "OK")
	b.SetDefault()
	buttons.AddButton(b)
	buttons.AddButton(wx.Button(self, wx.ID_CANCEL, "Cancel"))
	buttons.Realize()
	border = wx.BoxSizer(wx.VERTICAL)
	border.Add(fgs, 1, wx.GROW | wx.ALL, 25)
	border.Add(buttons)
	self.SetSizer(border)
	border.Fit(self)
	self.Layout()

