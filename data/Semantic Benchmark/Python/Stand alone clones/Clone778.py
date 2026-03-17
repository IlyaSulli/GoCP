def softmax(z) :
	assert len(z.shape) == 2
	s = np.max(z, axis = 1)
	s = s [:, np.newaxis]
	e_x = np.exp(z - s)
	div = np.sum(e_x, axis = 1)
	div = div [:, np.newaxis]
	return e_x / div


def softmax(X, theta = 1.0, axis = None) :
	y = np.atleast_2d(X)
	if axis is None :
		axis = next(j [0] for j in enumerate(y.shape) if j [1] > 1)
	y = y * float(theta)
	y = y - np.expand_dims(np.max(y, axis = axis), axis)
	y = np.exp(y)
	ax_sum = np.expand_dims(np.sum(y, axis = axis), axis)
	p = y / ax_sum
	if len(X.shape) == 1 : p = p.flatten()
	return p

