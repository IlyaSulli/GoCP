def __init__(self, widget) :
	logging.Handler.__init__(self)
	self.setLevel(logging.DEBUG)
	self.widget = widget
	self.widget.config(state = 'disabled')
	self.widget.tag_config("INFO", foreground = "black")
	self.widget.tag_config("DEBUG", foreground = "grey")
	self.widget.tag_config("WARNING", foreground = "orange")
	self.widget.tag_config("ERROR", foreground = "red")
	self.widget.tag_config("CRITICAL", foreground = "red", underline = 1)
	self.red = self.widget.tag_configure("red", foreground = "red")


def __init__(self, * args, ** kwargs) :
	ttk.Frame.__init__(self, * args, ** kwargs)
	self.columnconfigure(0, weight = 1)
	self.columnconfigure(1, weight = 0)
	self.rowconfigure(0, weight = 1)
	self.scrollbar = Scrollbar(self)
	self.scrollbar.grid(row = 0, column = 1, sticky = (N, S, E))
	self.text = Text(self, yscrollcommand = self.scrollbar.set)
	self.text.grid(row = 0, column = 0, sticky = (N, S, E, W))
	self.scrollbar.config(command = self.text.yview)
	self.logging_handler = LoggingHandlerFrame.Handler(self.text)

