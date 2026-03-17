def main() :
	q = Queue()
	p1 = Process(target = f1, args = (q,))
	p1.start()
	p2 = Process(target = f2, args = (q,))
	p2.start()
	while True :
		try :
			print q.get()
		except :
			break


def main() :
	p1 = Process(target = f1, args = ())
	p2 = Process(target = f2, args = ())
	p1.start()
	p2.start()
	p1.join()
	p2.join()

