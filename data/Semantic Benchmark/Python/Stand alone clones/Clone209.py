def traceit(frame, event, arg) :
	if event == "line" :
		lineno = frame.f_lineno
		filename = frame.f_globals ["__file__"]
		if filename == "<stdin>" :
			filename = "traceit.py"
		if (filename.endswith(".pyc") or
		filename.endswith(".pyo")) :
			filename = filename [: - 1]
		name = frame.f_globals ["__name__"]
		line = linecache.getline(filename, lineno)
		print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
	return traceit


def traceit(self, frame, event, arg) :
	if event == "line" :
		lineno = frame.f_lineno
		filename = frame.f_globals ["__file__"]
		if filename == "<stdin>" :
			filename = "traceit.py"
		if (filename.endswith(".pyc") or
		filename.endswith(".pyo")) :
			filename = filename [: - 1]
		name = frame.f_globals ["__name__"]
		line = linecache.getline(filename, lineno)
		if frame.f_back is self.lastframe :
			print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
		else :
			print "%s:%s:%s(%s)" % (name, lineno, frame.f_code.co_name, str.join(', ', ("%s=%r" % item for item in frame.f_locals.iteritems())))
			print "%s:%s:%s: %s" % (name, lineno, frame.f_code.co_name, line.rstrip())
		self.lastframe = frame.f_back
	return self.traceit

