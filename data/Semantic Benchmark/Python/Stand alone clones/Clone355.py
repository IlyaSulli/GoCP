def test_verify_file_existance(self) :
	file_name = 'Test.csv'
	file_path = '../../Data/VandV/Input_Reader/'
	try :
		verify_file_existance(file_path, file_name)
	except :
		print ("file not found")


def test_verify_file_existance(self) :
	try :
		file_name = 'Test.csv'
		file_path = '../../Data/VandV/Input_Reader/'
		verify_file_existance(file_path, file_name)
	except Exception as e :
		print ("\n\aError. Unable to locate File!\nError: {}").format(str(e))
		try :
			exit(0)
		except :
			sys.exit(1)

