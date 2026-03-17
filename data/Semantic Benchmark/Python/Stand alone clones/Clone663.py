def text(ctx, string, pos, theta = 0.0, face = 'Georgia', font_size = 18) :
	ctx.save()
	ctx.select_font_face(face, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
	ctx.set_font_size(font_size)
	fascent, fdescent, fheight, fxadvance, fyadvance = ctx.font_extents()
	x_off, y_off, tw, th = ctx.text_extents(string) [: 4]
	nx = - tw / 2.0
	ny = fheight / 2
	ctx.translate(pos [0], pos [1])
	ctx.rotate(theta)
	ctx.translate(nx, ny)
	ctx.move_to(0, 0)
	ctx.show_text(string)
	ctx.restore()


def text(self, text, x, y, rotation = 0, fontName = "Arial", fontSize = 10, verticalPadding = 0) :
	rotation = rotation * math.pi / 180
	self.ctx.select_font_face(fontName, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
	self.ctx.set_font_size(fontSize)
	fascent, fdescent, fheight, fxadvance, fyadvance = self.ctx.font_extents()
	self.ctx.save()
	self.ctx.translate(x, y)
	self.ctx.rotate(rotation)
	lines = text.split("\n")
	for i in xrange(len(lines)) :
		line = lines [i]
		xoff, yoff, textWidth, textHeight = self.ctx.text_extents(line) [: 4]
		offx = - textWidth / 2.0
		offy = (fheight / 2.0) + (fheight + verticalPadding) * i
		self.ctx.move_to(offx, offy)
		self.ctx.show_text(line)
	self.ctx.restore()

