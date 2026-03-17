def sierpinski(a, t, size) :
	if a == 0 :
		for i in range(3) :
			t.forward(size)
			t.left(120)
	else :
		sierpinski(a - 1, t, size / 2)
		t.forward(size / 2)
		sierpinski(a - 1, t, size / 2)
		t.forward(size / 2)
		t.left(120)
		t.forward(size / 2)
		sierpinski(a - 1, t, size / 2)
		t.forward(size / 2)
		t.left(120)
		t.forward(size)
		t.left(120)


def sierpinski(depth, turtle, size) :
	turtle.shapesize(size / CURSOR_SIZE)
	turtle.stamp()
	if depth < 1 :
		return
	half = size / 2
	circumradius = half * 3 ** 0.5 / 3
	for _ in range(3) :
		turtle.forward(circumradius)
		sierpinski(depth - 1, turtle, half)
		turtle.backward(circumradius)
		turtle.left(120)

