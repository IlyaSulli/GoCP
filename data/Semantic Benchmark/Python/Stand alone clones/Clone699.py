def tone(self, frequency, length = 1000, play = False, ** kwargs) :
	number_of_frames = int(self.bitrate * length / 1000.)
	phInc = 2 * math.pi * frequency / self.bitrate
	for x in xrange(number_of_frames) :
		y = math.sin(self._phase)
		_phase += phaseInc;
		self._queue.append(chr(int(y)))


def tone(self, frequency, length = 1000, play = False, ** kwargs) :
	number_of_frames = int(self.bitrate * length / 1000.)
	record = False
	x = 0
	y = 0
	while 1 :
		x += 1
		v = math.sin(x / ((self.bitrate / float(frequency)) / math.pi))
		if round(v, 3) == + 1 :
			record = True
		if record :
			self._queue.append(chr(int(v * 127 + 128)))
			y += 1
			if y > number_of_frames and round(v, 3) == + 1 :
				break

