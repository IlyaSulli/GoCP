def receive(self) :
	while True :
		try :
			record = self.queue.get()
			self._handler.emit(record)
		except (KeyboardInterrupt, SystemExit) :
			raise
		except EOFError :
			break
		except :
			traceback.print_exc(file = sys.stderr)


def receive(self) :
	while (self.shutdown == False) or (self.queue.empty() == False) :
		try :
			record = self.queue.get(True, self.polltime)
			self._handler.emit(record)
		except Queue.Empty, e :
			pass

