def Run(self) :
	self.time0 = time.clock()
	self.JobBeginning(self.duration)
	try :
		for count in range(0, self.duration) :
			time.sleep(1.0)
			self.JobProgress(count)
			self.PossibleStoppingPoint()
	except InterruptedException :
		print "canceled prematurely!"
	self.JobFinished()


def Run(self) :
	self.time0 = time.clock()
	try :
		source = open(self.src, 'rb')
		import os
		(st_mode, st_ino, st_dev, st_nlink, st_uid, st_gid, st_size, st_atime, st_mtime, st_ctime) = os.stat(self.src)
		num_blocks = st_size / self.block_size
		current_block = 0
		self.JobBeginning(num_blocks)
		dest = open(self.dest, 'wb')
		while 1 :
			copy_buffer = source.read(self.block_size)
			if copy_buffer :
				dest.write(copy_buffer)
				current_block += 1
				self.JobProgress(current_block)
				self.PossibleStoppingPoint()
			else :
				break
		source.close()
		dest.close()
	except InterruptedException :
		dest.close()
		os.unlink(self.dest)
		print "canceled, dest deleted!"
	self.JobFinished()

