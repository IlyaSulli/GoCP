def __init__(self, t) :
	self.i = Tkinter.PhotoImage(width = 100, height = 100)
	colors = [[random.randint(0, 255) for i in range(0, 3)] for j in range(0, 10000)]
	row = 0; col = 0
	for color in colors :
		self.i.put('#%02x%02x%02x' % tuple(color), (row, col))
		col += 1
		if col == 100 :
			row += 1; col = 0
	c = Tkinter.Canvas(t, width = 100, height = 100); c.pack()
	c.create_image(0, 0, image = self.i, anchor = Tkinter.NW)


def __init__(self, t) :
	self.width = 320
	self.height = 200
	self.i = Tkinter.PhotoImage(width = self.width, height = self.height)
	rgb_colors = ([random.randint(0, 255) for i in range(0, 3)] for j in range(0, self.width * self.height))
	pixels = " ".join(("{" + " ".join(('#%02x%02x%02x' %
	tuple(next(rgb_colors)) for i in range(self.width))) + "}" for j in range(self.height)))
	self.i.put(pixels, (0, 0, self.width - 1, self.height - 1))
	c = Tkinter.Canvas(t, width = self.width, height = self.height); c.pack()
	c.create_image(0, 0, image = self.i, anchor = Tkinter.NW)

