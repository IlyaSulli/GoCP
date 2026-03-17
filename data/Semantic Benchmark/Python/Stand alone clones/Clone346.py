def backupToZip(folder) :
	import zipfile, os
	folder = os.path.abspath(folder)
	for foldername, subfolders, filenames in os.walk(folder) :
		if foldername == folder :
			archive_folder_name = ''
		else :
			archive_folder_name = os.path.relpath(foldername, folder)
			backupZip.write(foldername, arcname = archive_folder_name)
		for filename in filenames :
			backupZip.write(os.path.join(foldername, filename), arcname = os.path.join(archive_folder_name, filename))
	backupZip.close()


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

