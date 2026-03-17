def decrypt(string, password) :
	key = password_to_key(password)
	IV = string [: AES.block_size]
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	string = decryptor.decrypt(string [AES.block_size :])
	return unpad_string(string)


def decrypt(key, source, decode = True) :
	if decode :
		source = base64.b64decode(source.encode("latin-1"))
	key = SHA256.new(key).digest()
	IV = source [: AES.block_size]
	decryptor = AES.new(key, AES.MODE_CBC, IV)
	data = decryptor.decrypt(source [AES.block_size :])
	padding = data [- 1]
	if data [- padding :] ! = bytes([padding]) * padding :
		raise ValueError("Invalid padding...")
	return data [: - padding]

