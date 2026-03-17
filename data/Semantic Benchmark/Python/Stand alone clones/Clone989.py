def spiral(width, height) :
	if width < 1 or height < 1 :
		raise ValueError
	x, y = width / / 2, height / / 2
	dx, dy = NORTH
	matrix = [[None] * width for _ in range(height)]
	count = 0
	while True :
		count += 1
		matrix [y] [x] = count
		new_dx, new_dy = turn_right [dx, dy]
		new_x, new_y = x + new_dx, y + new_dy
		if (0 < = new_x < width and 0 < = new_y < height and
		matrix [new_y] [new_x] is None) :
			x, y = new_x, new_y
			dx, dy = new_dx, new_dy
		else :
			x, y = x + dx, y + dy
			if not (0 < = x < width and 0 < = y < height) :
				return matrix


def spiral(X, Y) :
	x = y = 0
	dx = 0
	dy = - 1
	for i in range(max(X, Y) ** 2) :
		if (- X / 2 < x < = X / 2) and (- Y / 2 < y < = Y / 2) :
			yield x, y
		if x == y or (x < 0 and x == - y) or (x > 0 and x == 1 - y) :
			dx, dy = - dy, dx
		x, y = x + dx, y + dy
	spiral_matrix_size = 5
	my_list = list(range(spiral_matrix_size ** 2))
	my_list = [my_list [x : x + spiral_matrix_size] for x in range(0, len(my_list), spiral_matrix_size)]
	print (my_list)
	for i, (x, y) in enumerate(spiral(spiral_matrix_size, spiral_matrix_size)) :
		diff = int(spiral_matrix_size / 2)
		my_list [x + diff] [y + diff] = i
	print (my_list)

