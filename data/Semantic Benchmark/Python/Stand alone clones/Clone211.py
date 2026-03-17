def main() :
	q = queue.Queue()
	threads = [threading.Thread(target = func, args = (i, q)) for i in range(5)]
	for th in threads :
		th.daemon = True
		th.start()
	result1 = q.get()
	result2 = q.get()
	print ("Second result: {}".format(result2))


def main() :
	print 'testing this stuff'
	def func(i) :
		import time, random
		sleeptime = (random.random() * 2) + 1
		print 'thread', i, 'starting - sleep for', sleeptime
		time.sleep(sleeptime)
		print 'thread', i, 'finished'
	threads = [MWThread(target = func, args = (i,)) for i in range(3)]
	for th in threads :
		th.start()
	i = 0
	while i < 3 :
		print 'main: wait up to .5 sec'
		th = wait_for_thread(.5)
		if th :
			print 'main: got', th
			th.join()
			i += 1
		else :
			print 'main: timeout'
	print 'I think I collected them all'
	print 'result of wait_for_thread():'
	print wait_for_thread()

