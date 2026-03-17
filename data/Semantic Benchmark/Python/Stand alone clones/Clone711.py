def __init__(self) :
	self.root = Tk.Tk()
	self.root.wm_title("Fibonacci Calculator")
	self.root.wm_iconbitmap("@icon2.xbm")
	Tk.Label(self.root, text = "Set the digit number you want.").pack()
	self.digits = Tk.StringVar()
	Tk.Entry(self.root, textvariable = self.digits).pack()
	Tk.Button(self.root, text = "Calculate", command = self.clicked).pack()
	self.result = Tk.Label(self.root, text = " ")
	self.result.pack()
	self.root.mainloop()


def __init__(self) :
	self.root = Tk.Tk()
	self.root.wm_title("Fibonacci Calculator")
	self.label = Tk.Label(self.root, text = "Set the digit number you want.")
	self.label.pack()
	self.digits = Tk.StringVar()
	Tk.Entry(self.root, textvariable = self.digits).pack()
	self.buttontext = Tk.StringVar()
	self.buttontext.set("Calculate")
	Tk.Button(self.root,
	textvariable = self.buttontext,
	command = self.clicked1).pack()
	self.label = Tk.Label(self.root, text = " ")
	self.label.pack()
	self.root.mainloop()

