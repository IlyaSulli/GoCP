def game_intro() :
	intro = True
	while intro :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				quit()
			mouse = pygame.mouse.get_pos()
			if 150 + 100 > mouse [0] > 150 and 430 + 50 > mouse [1] > 430 :
				pygame.draw.rect(gameDisplay, bright_green, (150, 430, 100, 50))
			else :
				pygame.draw.rect(gameDisplay, green, (150, 430, 100, 50))


def game_intro() :
	intro = True
	while intro :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				quit()
	gameDisplay.fill(white)
	largeText = pygame.font.Font('freesansbold.ttf', 90)
	TextSurf, TextRect = text_objects("Run Abush Run!", largeText)
	TextRect.center = ((display_width / 2), (display_height / 2))
	gameDisplay.blit(TextSurf, TextRect)
	mouse = pygame.mouse.get_pos()
	if 150 + 100 > mouse [0] > 150 and 450 + 50 > mouse [1] > 450 :
		pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
	else :
		pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
	pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
	pygame.display.update()
	clock.tick(15)

