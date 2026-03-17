def backupToZip(folder) :
	cwdpath = os.getcwd()
	saveToWhere = "tmp.zip"
	zf = zipfile.ZipFile(saveToWhere, mode = 'w')
	folder = os.path.abspath(folder)
	os.chdir(folder)
	for foldername, subfolders, filenames in os.walk("./") :
		for filename in filenames :
			zf.write(os.path.join(foldername, filename))
	zf.close()
	os.chdir(cwdpath)


def backupToZip(folder) :
	folder = os.path.abspath(folder)
	backupZip = zipfile.ZipFile('backup.zip', 'w')
	backupZip.write(folder, arcname = os.path.basename(folder))
	for foldername, subfolders, filenames in os.walk(folder) :
		if foldername ! = folder :
			backupZip.write(foldername, arcname = os.path.relpath(foldername, os.path.dirname(folder)))
		for filename in filenames :
			backupZip.write(os.path.join(foldername, filename), arcname = os.path.join(os.path.relpath(foldername, os.path.dirname(folder)), filename))
	backupZip.close()

