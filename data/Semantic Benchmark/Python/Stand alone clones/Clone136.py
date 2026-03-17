def customop(qstat) :
	dimensions = input("What are the dimensions of your (square) matrix? Please input a single number: ")
	matrix = np.zeros([dimensions, dimensions])
	for iterator in range(dimensions) :
		for iterator_2 in range(dimensions) :
			matrix [iterator, iterator_2] = float(input("Matrix element at " + str(iterator) + "," + str(iterator_2) + ": "))
	if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(2)) == True :
		print (matrix)
		return np.dot(matrix, qstat)
	else :
		print (matrix)
		print ("matrix not unitary, pretending no gate was applied")
		return qstat


def customop(qstat) :
	dimensions = int(input("What are the dimensions of your (square) matrix? Please input a single number: "))
	iterator = 1
	iterator_2 = 1
	elements = []
	while iterator < = dimensions :
		while iterator_2 < = dimensions :
			elements.append(float(input("Matrix element at " + str(iterator) + "," + str(iterator_2) + ": ")))
			iterator_2 += 1
		iterator_2 = 1
		iterator += 1
	matrix = np.matrix(elements).reshape(dimensions, dimensions)
	if np.array_equal(np.dot(matrix, matrix.conj().T), np.identity(2)) == True :
		print (matrix)
		return np.dot(matrix, qstat)
	else :
		print (matrix)
		print ("matrix not unitary, pretending no gate was applied")
		return qstat

