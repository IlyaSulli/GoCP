def polyfit2d(x, y, f, deg) :
	from numpy.polynomial import polynomial
	import numpy as np
	x = np.asarray(x)
	y = np.asarray(y)
	f = np.asarray(f)
	deg = np.asarray(deg)
	vander = polynomial.polyvander2d(x, y, deg)
	vander = vander.reshape((- 1, vander.shape [- 1]))
	f = f.reshape((vander.shape [0],))
	c = np.linalg.lstsq(vander, f) [0]
	return c.reshape(deg + 1)


def polyfit2d(x, y, z, order = 3) :
	ncols = (order + 1) ** 2
	G = np.zeros((x.size, ncols))
	ij = itertools.product(range(order + 1), range(order + 1))
	for k, (i, j) in enumerate(ij) :
		G [:, k] = x ** i * y ** j
	m, _, _, _ = np.linalg.lstsq(G, z)
	return m

