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
	folder = os.path.abspath(folder)
	backupZip = zipfile.ZipFile('backup.zip', 'w')
	backupZip.write(folder, arcname = os.path.basename(folder))
	for foldername, subfolders, filenames in os.walk(folder) :
		if foldername ! = folder :
			backupZip.write(foldername, arcname = os.path.relpath(foldername, os.path.dirname(folder)))
		for filename in filenames :
			backupZip.write(os.path.join(foldername, filename), arcname = os.path.join(os.path.relpath(foldername, os.path.dirname(folder)), filename))
	backupZip.close()

