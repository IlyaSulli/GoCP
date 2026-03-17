def __init__(self) :
	self.secondsRemaining = 10.0
	self.lastTick = 0
	self.isPaused = False
	self.isRunning = False
	self.keepGoing = True


def __init__(self, parent, job) :
	self.job = job
	wx.Dialog.__init__(self, parent, - 1, "Progress", size = (350, 200))
	sizeAll = wx.BoxSizer(wx.VERTICAL)
	self.JobStatusText = wx.StaticText(self, - 1, "Starting...")
	sizeAll.Add(self.JobStatusText, 0, wx.EXPAND | wx.ALL, 8)
	self.ProgressBar = wx.Gauge(self, - 1, 10, wx.DefaultPosition, (250, 15))
	sizeAll.Add(self.ProgressBar, 0, wx.EXPAND | wx.ALL, 8)
	sizeRemaining = wx.BoxSizer(wx.HORIZONTAL)
	sizeRemaining.Add((2, 2), 1, wx.EXPAND)
	self.remainingText = wx.StaticText(self, - 1, "???:??")
	sizeRemaining.Add(self.remainingText, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 8)
	self.remainingLabel = wx.StaticText(self, - 1, "remaining")
	sizeRemaining.Add(self.remainingLabel, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 8)
	sizeAll.Add(sizeRemaining, 1, wx.EXPAND)
	sizeButtons = wx.BoxSizer(wx.HORIZONTAL)
	sizeButtons.Add((2, 2), 1, wx.EXPAND | wx.ADJUST_MINSIZE)
	self.PauseButton = wx.Button(self, - 1, "Pause")
	sizeButtons.Add(self.PauseButton, 0, wx.ALL, 4)
	self.Bind(wx.EVT_BUTTON, self.OnPauseButton, self.PauseButton)
	self.CancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")
	sizeButtons.Add(self.CancelButton, 0, wx.ALL, 4)
	self.Bind(wx.EVT_BUTTON, self.OnCancel, self.CancelButton)
	sizeAll.Add(sizeButtons, 0, wx.EXPAND | wx.ALL, 4)
	self.SetSizer(sizeAll)
	sizeAll.SetSizeHints(self)
	self.Bind(EVT_PROGRESS_START, self.OnProgressStart)
	self.Bind(EVT_PROGRESS, self.OnProgress)
	self.Bind(EVT_DONE, self.OnDone)
	self.Layout()

