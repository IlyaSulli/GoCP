def run(self) :
	while True :
		log_level, message = self.queue.get()
		if log_level is None :
			self.log.info("Shutting down Central Logging process")
			break
		else :
			self.log.log(log_level, message)


def run(self) :
	while True :
		try :
			record = self.queue.get()
			logger = logging.getLogger(record.name)
			logger.callHandlers(record)
		except (KeyboardInterrupt, SystemExit) :
			raise
		except EOFError :
			break
		except :
			traceback.print_exc(file = sys.stderr)

