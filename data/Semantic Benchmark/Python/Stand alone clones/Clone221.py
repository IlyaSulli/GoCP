def __init__(self, * args, ** kwargs) :
	tk.Tk.__init__(self, * args, ** kwargs)
	self.frame = tk.Frame(self)
	self.frame.pack(side = "top", fill = "both", expand = True)
	self.label = tk.Label(self, text = "Hello, world")
	button1 = tk.Button(self, text = "Click to hide label",
	command = self.hide_label)
	button2 = tk.Button(self, text = "Click to show label",
	command = self.show_label)
	self.label.pack(in_ = self.frame)
	button1.pack(in_ = self.frame)
	button2.pack(in_ = self.frame)


def __init__(self, parent, title = "How to Cheat and Hide Text") :
	Toplevel.__init__(self, parent)
	parent.geometry("250x250+100+150")
	if title :
		self.title(title)
	parent.withdraw()
	self.parent = parent
	self.result = None
	dialog = Frame(self)
	self.initial_focus = self.dialog(dialog)
	dialog.pack()

