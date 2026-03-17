def calculate_speed(radius) :
	global speeds, speed_idx
	t1 = time.time()
	speeds [speed_idx] = radius / (t1 - t0)
	print (sum(speeds) / iterations, 'mm/sek')
	speed_idx += 1
	speed_idx %= iterations


def calculate_speed(radius) :
	global t0
	t1 = time.clock
	interval = t1 - t0
	speed = radius / interval
	print (speed, 'mm/sek')
	speed_records.append(speed)
	if len(speed_records) > = 5 :
		last_five_records = speed_records [- 5 :]
		average = sum(last_five_records) / 5
		print ('Average Speed:', average)
	if len(speed_records) > 10 :
		speed_records = list(set(speed_records) - set(speed_records [: 5]))

