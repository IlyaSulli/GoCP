def data(self, index, role = Qt.DisplayRole) :
	if index.isValid() :
		col = index.column()
		spot = self.items [index.row()]
		if role == Qt.DisplayRole :
			if col == 0 or col == 1 :
				return self.items [index.row()] [col]
			elif col == 2 :
				return self.items [index.row()] [0] + self.items [index.row()] [1]
			elif col == 3 :
				return self.items [index.row()] [2]


def data(self, index, role = QtCore.Qt.DisplayRole) :
	if role == QtCore.Qt.DisplayRole and index.column() == 2 :
		return sum(self.data(self.index(index.row(), i)).toInt() [0] for i in range(2))
	if index.column() > 2 :
		index = self.index(index.row(), index.column() - 1)
	return super(Model, self).data(index, role)

