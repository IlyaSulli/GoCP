def __init__(self) :
	tk.Tk.__init__(self)
	self.queue = queue.Queue()
	self.listbox = tk.Listbox(self, width = 20, height = 5)
	self.progressbar = ttk.Progressbar(self, orient = 'horizontal',
	length = 300, mode = 'determinate')
	self.button = tk.Button(self, text = "Start", command = self.spawnthread)
	self.listbox.pack(padx = 10, pady = 10)
	self.progressbar.pack(padx = 10, pady = 10)
	self.button.pack(padx = 10, pady = 10)


def __init__(self) :
	self.root = tkinter.Tk()
	self.int_var = tkinter.IntVar()
	progbar = ttk.Progressbar(self.root, maximum = 4)
	progbar ['variable'] = self.int_var
	progbar.pack()
	self.label = ttk.Label(self.root, text = '0/4')
	self.label.pack()
	self.b_start = ttk.Button(self.root, text = 'Start')
	self.b_start ['command'] = self.start_thread
	self.b_start.pack()

