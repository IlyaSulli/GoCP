def find_items_within(list1, list2, within) :
	i2_idx = 0
	shared = []
	for i1 in list1 :
		while shared and abs(shared [0] - i1) > within :
			shared.pop(0)
		while i2_idx < len(list2) and abs(list2 [i2_idx] - i1) < = within :
			shared.append(list2 [i2_idx])
			i2_idx += 1
		for result in zip([i1] * len(shared), shared) :
			yield result


def find_items_within(l1, l2, dist) :
	l1.sort()
	l2.sort()
	b = 0
	e = 0
	ans = []
	for a in l1 :
		while b < len(l2) and a - l2 [b] > dist :
			b += 1
		while e < len(l2) and l2 [e] - a < = dist :
			e += 1
		ans.extend([(a, x) for x in l2 [b : e]])
	return ans

