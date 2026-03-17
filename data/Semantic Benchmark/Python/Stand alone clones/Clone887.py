def detect_color_image(file) :
	v = ImageStat.Stat(Image.open(file)).var
	is_monochromatic = reduce(lambda x, y : x and y < MONOCHROMATIC_MAX_VARIANCE, v, True)
	print file, '-->\t',
	if is_monochromatic :
		print "Monochromatic image",
	else :
		if len(v) == 3 :
			maxmin = abs(max(v) - min(v))
			if maxmin > COLOR :
				print "Color\t\t\t",
			elif maxmin > MAYBE_COLOR :
				print "Maybe color\t",
			else :
				print "grayscale\t\t",
			print "(", maxmin, ")"
		elif len(v) == 1 :
			print "Black and white"
		else :
			print "Don't know..."


def detect_color_image(file, thumb_size = 40, MSE_cutoff = 22, adjust_color_bias = True) :
	pil_img = Image.open(file)
	bands = pil_img.getbands()
	if bands == ('R', 'G', 'B') or bands == ('R', 'G', 'B', 'A') :
		thumb = pil_img.resize((thumb_size, thumb_size))
		SSE, bias = 0, [0, 0, 0]
		if adjust_color_bias :
			bias = ImageStat.Stat(thumb).mean [: 3]
			bias = [b - sum(bias) / 3 for b in bias]
		for pixel in thumb.getdata() :
			mu = sum(pixel) / 3
			SSE += sum((pixel [i] - mu - bias [i]) * (pixel [i] - mu - bias [i]) for i in [0, 1, 2])
		MSE = float(SSE) / (thumb_size * thumb_size)
		if MSE < = MSE_cutoff :
			print "grayscale\t",
		else :
			print "Color\t\t\t",
		print "( MSE=", MSE, ")"
	elif len(bands) == 1 :
		print "Black and white", bands
	else :
		print "Don't know...", bands

