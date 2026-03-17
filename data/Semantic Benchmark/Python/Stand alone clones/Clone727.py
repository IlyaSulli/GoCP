def test() :
	import time
	def m_int(s, memo = {}) :
		if s in memo :
			return memo [s]
		else :
			retval = memo [s] = int(s)
			return retval
	data = get_data()
	all_point_sets = []
	time_start = time.time()
	for xs, ys in data :
		point_set = []
		y_iter = iter(ys.split(","))
		curr_points = [Point(m_int(i), m_int(next(y_iter))) for i in xs.split(",")]
		all_point_sets.append(curr_points)
	time_end = time.time()
	print "total time: ", (time_end - time_start)


def test(data) :
	all_point_sets = []
	for row in data :
		point_set = []
		first_points, second_points = row
		first_points = map(int, first_points.split(","))
		second_points = map(int, second_points.split(","))
		paired_points = zip(first_points, second_points)
		curr_points = [Point(p [0], p [1]) for p in paired_points]
		all_point_sets.append(curr_points)
	return all_point_sets

