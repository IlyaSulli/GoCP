def main() :
	pygame.init()
	white = (255, 255, 255)
	red = (255, 0, 0)
	gameDisplay = pygame.display.set_mode((600, 800))
	gameExit = False
	x = 0
	y = 0
	w = 25
	h = 25
	sobj = shape(white, 0, 0, 25, 25)
	sobj.draw_rect(gameDisplay)


def main() :
	game_display = pygame.display.set_mode((600, 800))
	shape = Shape(WHITE, 0, 0, 25, 25)
	shape2 = Shape(pygame.Color('sienna1'), 100, 100, 25, 25)
	clock = pygame.time.Clock()
	game_exit = False
	while not game_exit :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				game_exit = True
		game_display.fill((40, 40, 40))
		shape.draw(game_display)
		shape2.draw(game_display)
		pygame.display.update()
		clock.tick(60)

