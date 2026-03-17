def draw(self, win, rows, columns) :
	for day, (start, length) in self.schedule :
		box = Rectangle(
		Point(columns [day], rows [start]),
		Point(columns [day + 1], rows [start + length]))
		box.setFill(self.bg)
		box.setOutline(self.border)
		box.draw(win)
		label = Text(Point(columns [day] + 10, rows [start] + 40), self.name)
		label.fontSize = 9
		label.setFill(self.text)
		label.draw(win)


def draw(self, win, left, top, width, height) :
	label_space = 40
	label = Text(Point(Point(left + 0.5 * width, top + 0.5 * label_space)), self.label)
	label.fontSize = 20
	label.setFill(Black)
	label.draw(win)
	days = 5
	columns = [left + width * n / days for n in range(days + 1)]
	periods = 5
	rows = [top + label_space + (height - label_space) * n / periods for n in range(periods + 1)]
	for p in self.periods :
		p.draw(win, rows, columns)

