def __init__(self, pos, checkpoints) :
	super().__init__()
	self.image = pg.Surface((60, 60), pg.SRCALPHA)
	pg.draw.polygon(self.image, (0, 100, 240), [(30, 0), (60, 60), (0, 60)])
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)
	self.checkpoints = itertools.cycle(checkpoints)
	self.active_checkpoint = next(self.checkpoints)
	self.start_point = self.active_checkpoint
	self.active_checkpoint.image = self.active_checkpoint.image_active
	self.laps = - 1


def __init__(self) :
	self.screen = pg.display.set_mode((640, 480))
	self.done = False
	self.clock = pg.time.Clock()
	self.checkpoints = (
	Checkpoint((100, 200), 0),
	Checkpoint((300, 100), 60),
	Checkpoint((500, 300), 10),
	Checkpoint((200, 300), 30),
	)
	self.player = Player((20, 20), self.checkpoints)
	self.all_sprites = pg.sprite.Group(self.player)
	self.all_sprites.add(self.checkpoints)

