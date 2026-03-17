def read(self, block_size = None) :
	block_size = block_size or self._block_size
	total_read = 0
	chunks = []
	for chunk in self._reader :
		chunks.append(chunk)
		total_read += len(chunk)
		if total_read > block_size :
			contents = ''.join(chunks)
			self._reader = chain([contents [block_size :]], self._reader)
			return contents [: block_size]
	return ''.join(chunks)


def read(self, size = None) :
	remaining = size
	data = StringIO()
	while self.fds and (remaining > 0 or remaining is None) :
		data_read = self.fds [- 1].read(remaining or - 1)
		if len(data_read) < remaining or remaining is None :
			self.fds.pop()
		if not remaining is None :
			remaining -= len(data_read)
		data.write(data_read)
	return data.getvalue()

