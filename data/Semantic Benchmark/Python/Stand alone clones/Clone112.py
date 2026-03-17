def print_checked_items(self) :
	path = "/home/test1/checked.txt"
	mode = QtCore.QFile.Append if self.isWritten else QtCore.QFile.WriteOnly
	if len(self.items) > 0 :
		file = QtCore.QFile(path)
		if file.open(mode) :
			for item in self.items :
				print ('%s' % item.text())
				file.write(item.text() + "\n")
		file.close()
	print ("print checked items executed")


def print_checked_items(self) :
	for index in range(self.model.rowCount()) :
		item = self.model.item(index)
		if item.checkState() == QtCore.Qt.Checked :
			if self.isWritten :
				mode = "a"
			else :
				mode = "w"
				self.isWritten = True
			print ('%s' % item.text())
	print ("print checked items executed")

