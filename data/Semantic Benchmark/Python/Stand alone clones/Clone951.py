def __init__(self) :
	platform = pyglet.window.get_platform()
	display = platform.get_default_display()
	screen = display.get_default_screen()
	self.widthScreen = screen.width
	self.heightScreen = screen.height
	self.xDisplay = int(self.widthScreen / 2 - self.widthDisplay / 2)
	self.yDisplay = int(self.heightScreen / 2 - self.heightDiplay / 2)
	self.Display = pyglet.window.Window(width = self.widthDisplay, height = self.heightDiplay, caption = self.title, resizable = False)
	self.Display.set_location(self.xDisplay, self.yDisplay)
	pyglet.app.run()


def __init__(self, width = 1024, height = 576, caption = "Pokémon Life and Death: Esploratori del proprio Destino", fps = True, * args, ** kwargs) :
	super(main, self).__init__(width, height, * args, ** kwargs)
	platform = pyglet.window.get_platform()
	display = platform.get_default_display()
	screen = display.get_default_screen()
	self.xDisplay = int(screen.width / 2 - self.width / 2)
	self.yDisplay = int(screen.height / 2 - self.height / 2)
	self.set_location(self.xDisplay, self.yDisplay)
	self.sprites = OrderedDict()
	if fps :
		self.sprites ['fps_label'] = pyglet.text.Label('0 fps', x = 10, y = 10)
		self.last_update = time()
		self.fps_count = 0
	self.keys = OrderedDict()
	self.mouse_x = 0
	self.mouse_y = 0
	self.alive = 1

