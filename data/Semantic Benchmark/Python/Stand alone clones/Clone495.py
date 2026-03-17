def device_id_replace(filepath) :
	original_id = input("What device ID are you needing to replace?")
	new_id = input("What is the new device ID?")
	with open(filepath, 'r+') as devicetxt :
		string = devicetxt.read()
		string = string.replace(original_id, new_id)
		devicetxt.truncate(0)
		devicetxt.seek(0)
		devicetxt.write(string)


def device_id_replace(filepath) :
	original_id = input("What device ID are you needing to replace?")
	new_id = input("What is the new device ID?")
	with open(filepath, 'r+') as devicetxt :
		contents = devicetxt.readlines()
		for line_i, line in enumerate(contents) :
			if original_id in line :
				contents [line_i] = line.replace(original_id, new_id)
		devicetxt.truncate(0)
		devicetxt.seek(0)
		devicetxt.writelines(contents)

