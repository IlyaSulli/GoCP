def download(url, fileName = None) :
	def getFileName(url, openUrl) :
		if 'Content-Disposition' in openUrl.info() :
			cd = dict(map(
			lambda x : x.strip().split('=') if '=' in x else (x.strip(), ''),
			openUrl.info() ['Content-Disposition'].split(';')))
			if 'filename' in cd :
				filename = cd ['filename'].strip("\"'")
				if filename : return filename
		return os.path.basename(urlparse.urlsplit(openUrl.url) [2])
	r = urllib2.urlopen(urllib2.Request(url))
	try :
		fileName = fileName or getFileName(url, r)
		with open(fileName, 'wb') as f :
			shutil.copyfileobj(r, f)
	finally :
		r.close()


def download(url, localFileName = None) :
	localName = url2name(url)
	req = urllib2.Request(url)
	r = urllib2.urlopen(req)
	if r.info().has_key('Content-Disposition') :
		localName = r.info() ['Content-Disposition'].split('filename=') [1]
		if localName [0] == '"' or localName [0] == "'" :
			localName = localName [1 : - 1]
	elif r.url ! = url :
		localName = url2name(r.url)
	if localFileName :
		localName = localFileName
	f = open(localName, 'wb')
	f.write(r.read())
	f.close()

