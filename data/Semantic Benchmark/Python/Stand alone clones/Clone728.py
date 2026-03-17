def test2() :
	import json
	import time
	time_start = time.time()
	with open('data.csv', 'rb') as f :
		data = f.read()
	data = '[[[' + ']],[['.join(data.splitlines()).replace('\t', '],[') + ']]]'
	all_point_sets = [Point(* xy) for row in json.loads(data) for xy in zip(* row)]
	time_end = time.time()
	print "total time: ", (time_end - time_start)


def test2() :
	import time
	import gc
	data = get_data()
	all_point_sets = []
	gc.disable()
	time_start = time.time()
	for index, row in enumerate(data) :
		first_points, second_points = row
		first_points = [int(i) for i in first_points.split(",")]
		second_points = [int(i) for i in second_points.split(",")]
		curr_points = [(x, y) for x, y in zip(first_points, second_points)]
		all_point_sets.append(curr_points)
	time_end = time.time()
	gc.enable()
	print "variant 2 total time: ", (time_end - time_start)

