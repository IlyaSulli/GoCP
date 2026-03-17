def merge(arr1, arr2) :
	merged = []
	while arr1 and arr2 :
		if arr1 [0] > arr2 [0] :
			arr1, arr2 = arr2, arr1
		merged.append(arr1.pop(0))
	merged.extend(arr1 or arr2)
	return merged


def merge(arr1, arr2) :
	for i in arr1 :
		for j in list(range(len(arr2))) :
			if i < arr2 [j] :
				arr2.append(arr2 [- 1])
				for count in list(range(len(arr2) - 1, j, - 1)) :
					arr2 [count] = arr2 [count - 1]
				arr2 [j] = i
				break
			if j == len(arr2) - 1 :
				arr2.append(i)
	return arr2

