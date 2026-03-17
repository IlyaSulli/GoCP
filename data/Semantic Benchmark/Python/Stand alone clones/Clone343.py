def upload(path) :
	with open(path, 'rb') as file :
		try :
			ftp.storbinary("STOR " + os.path.basename(path), file)
		except ftplib.error_temp as error :
			return path, error
		else :
			return path, None


def upload(t) :
	server = locker.server, user = locker.user, password = locker.password, service = locker.service
	try :
		ftp = ftplib.FTP(server)
		ftp.login(user = user, passwd = password, acct = "")
		ftp.storbinary("STOR " + t.split('/') [- 1], open(t, "rb"))
		ftp.close()
	except ftplib.error_temp :
		ftp.close()
		sleep(2)
		upload(t)

