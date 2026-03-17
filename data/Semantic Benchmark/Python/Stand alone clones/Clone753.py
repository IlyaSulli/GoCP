def numpy_ewma(data, window) :
	returnArray = np.empty((data.shape [0]))
	returnArray.fill(np.nan)
	e = data [0]
	alpha = 2 / float(window + 1)
	for s in range(data.shape [0]) :
		e = ((data [s] - e) * alpha) + e
		returnArray [s] = e
	return returnArray


def numpy_ewma(data, window) :
	alpha = 2 / (window + 1.0)
	scale = 1 / (1 - alpha)
	n = data.shape [0]
	scale_arr = (1 - alpha) ** (- 1 * np.arange(n))
	weights = (1 - alpha) ** np.arange(n)
	pw0 = (1 - alpha) ** (n - 1)
	mult = data * pw0 * scale_arr
	cumsums = mult.cumsum()
	out = cumsums * scale_arr [: : - 1] / weights.cumsum()
	return out

