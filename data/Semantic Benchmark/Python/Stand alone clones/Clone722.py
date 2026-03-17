def update_position(self) :
	rotation = self.get_rotation()
	self.set_rotation(0)
	self.set_va(self.__Va)
	self.set_ha(self.__Ha)
	renderer = self.axes.figure.canvas.get_renderer()
	bbox1 = self.get_window_extent(renderer = renderer)
	self.set_va('center')
	self.set_ha('center')
	bbox2 = self.get_window_extent(renderer = renderer)
	dr = np.array(bbox2.get_points() [0] - bbox1.get_points() [0])
	rad = np.deg2rad(rotation)
	rot_mat = np.array([
	[np.cos(rad), np.sin(rad)],
	[- np.sin(rad), np.cos(rad)]])
	drp = np.dot(dr, rot_mat)
	offset = matplotlib.transforms.Affine2D().translate(- drp [0], - drp [1])
	self.set_rotation(rotation)
	return offset


def update_position(self) :
	self.set_rotation(0)
	self.set_va(self.__Va)
	self.set_ha(self.__Ha)
	self.set_position(self.__Position)
	ax = self.axes
	xy = self.__Position
	xlim = ax.get_xlim()
	ylim = ax.get_ylim()
	figW, figH = ax.get_figure().get_size_inches()
	_, _, w, h = ax.get_position().bounds
	aspect = ((figW * w) / (figH * h)) * (ylim [1] - ylim [0]) / (xlim [1] - xlim [0])
	renderer = ax.figure.canvas.get_renderer()
	bbox1 = self.get_window_extent(renderer = renderer)
	bbox1d = ax.transData.inverted().transform(bbox1)
	width = bbox1d [1, 0] - bbox1d [0, 0]
	height = bbox1d [1, 1] - bbox1d [0, 1]
	self.set_va('center')
	self.set_ha('center')
	bbox2 = self.get_window_extent(renderer = renderer)
	bbox2d = ax.transData.inverted().transform(bbox2)
	dr = np.array(bbox2d [0] - bbox1d [0])
	rad = np.deg2rad(self.__Rotation)
	rot_mat = np.array([
	[math.cos(rad), math.sin(rad) * aspect],
	[- math.sin(rad) / aspect, math.cos(rad)]])
	drp = np.dot(dr, rot_mat)
	self.set_position((xy [0] - drp [0], xy [1] - drp [1]))
	self.set_rotation(self.__Rotation)

