def start(* args, ** kw) :
	def run() :
		try :
			th.ret = f(* args, ** kw)
		except :
			th.exc = sys.exc_info()
	def get(timeout = None) :
		th.join(timeout)
		if th.exc :
			raise th.exc [0], th.exc [1], th.exc [2]
		return th.ret
	th = threading.Thread(None, run)
	th.exc = None
	th.get = get
	th.start()
	return th


def start(self, params) :
	self.data = None
	if self.thread is not None :
		if self.thread.isAlive() :
			return 'running'
	self.thread = threading.Thread(target = self.func, args = params)
	self.thread.start()
	return 'started'

