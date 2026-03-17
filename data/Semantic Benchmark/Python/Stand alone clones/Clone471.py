def is_cgi(self) :
	collapsed_path = CGIHTTPServer._url_collapse_path(self.path)
	dir_sep = collapsed_path.find('/', 1)
	head, tail = collapsed_path [: dir_sep], collapsed_path [dir_sep + 1 :]
	if head in self.cgi_directories :
		if not tail.endswith('.html') :
			self.cgi_info = head, tail
			return True
	return False


def is_cgi(self) :
	mime = MimeTypes()
	request = self.path.split('?')
	if len(request) == 2 :
		path, args = request
	else :
		path, args = request, None
	if isinstance(path, list) :
		path = path [0]
	url = urllib.pathname2url(path)
	mime_type = mime.guess_type(url)
	if 'python' in mime_type [0] :
		self.cgi_info = '', self.path [1 :]
		return True
	else :
		self.cgi_info = '', '/static.py?path=%s' % path [1 :]
		print self.cgi_info
		return True

