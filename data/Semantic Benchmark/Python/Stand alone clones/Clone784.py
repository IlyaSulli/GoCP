def paintEvent(self, event) :
	super(MySlider, self).paintEvent(event)
	qp = QPainter(self)
	pen = QPen()
	pen.setWidth(2)
	pen.setColor(Qt.black)
	qp.setPen(pen)
	font = QFont('Times', 10)
	qp.setFont(font)
	self.setContentsMargins(50, 50, 50, 50)
	self.setFixedSize(QSize(slider_x, slider_y))
	contents = self.contentsRect()
	max = self.maximum()
	min = self.minimum()
	y_inc = slider_y - (slider_y - groove_y) / 2
	for i in range(len(slider_step)) :
		qp.drawText(contents.x() - 2 * font.pointSize(), y_inc + font.pointSize() / 2, '{0:3}'.format(slider_step [i]))
		qp.drawLine(contents.x() + 2 * font.pointSize(), y_inc, contents.x() + contents.width(), y_inc)
		y_inc -= groove_y / (max - min)


def paintEvent(self, event) :
	super(MySlider, self).paintEvent(event)
	qp = QPainter(self)
	pen = QPen()
	pen.setWidth(2)
	pen.setColor(Qt.red)
	qp.setPen(pen)
	font = QFont('Times', 10)
	qp.setFont(font)
	self.setContentsMargins(50, 50, 50, 50)
	contents = self.contentsRect()
	self.setFixedSize(QSize(slider_x, slider_y))
	max_slider = self.maximum()
	min_slider = self.minimum()
	len_slider = max_slider - min_slider
	height = self.height()
	opt = QStyleOptionSlider()
	handle = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)
	handle_height = handle.height()
	height_diff = height - handle_height
	point_size = font.pointSize()
	for i in range(max_slider) :
		y = round(((1 - i / len_slider) * height_diff + (handle_height / 2.0))) - 1
		if i == 0 :
			y = self.height() - handle_height / 2.0
		qp.drawText(contents.x() - point_size, y + point_size / 2, '{0:2}'.format(slider_step [len_slider - i]))
		qp.drawLine(contents.x() + point_size, y, contents.x() + contents.width(), y)

