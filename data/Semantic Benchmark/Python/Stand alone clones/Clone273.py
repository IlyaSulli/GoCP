def unique_file(input_filename, output_filename) :
	with open(input_filename) as file :
		contents = file.read()
		word_set = set(contents.split())
	with open(output_filename, "w+") as output_file :
		for word in word_set :
			output_file.write(word + '\n')
	print ("Done")


def unique_file(input_filename, output_filename) :
	file = open(input_filename, "r")
	contents = file.read()
	word_list = contents.split()
	output_file = open(output_filename, 'w+')
	seen = set()
	for word in word_list :
		if word not in seen :
			output_file.write(word + '\n')
		seen.add(word)
	file.close()
	output_file.close()
	print ('Done')

