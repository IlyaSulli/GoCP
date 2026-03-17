def run(self) :
	t = datetime(* datetime.now().timetuple() [: 5])
	while 1 :
		for e in self.events :
			e.check(t)
		t += timedelta(minutes = 1)
		n = datetime.now()
		while n < t :
			s = (t - n).seconds + 1
			time.sleep(s)
			n = datetime.now()


def run(self) :
	while 1 :
		t = datetime.now()
		for e in self.events :
			e.check(t)
		time.sleep(60 - t.second - t.microsecond / 1000000.0)

