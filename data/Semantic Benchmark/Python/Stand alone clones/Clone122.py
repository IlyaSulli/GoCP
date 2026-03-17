def __init__(self, pos, angle = 0) :
	super().__init__()
	self.image_inactive = pg.transform.rotate(CHECKPOINT_IMG, angle)
	self.image_active = pg.transform.rotate(CHECKPOINT2_IMG, angle)
	self.image = self.image_inactive
	self.rect = self.image.get_rect(center = pos)
	self.mask = pg.mask.from_surface(self.image)


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

