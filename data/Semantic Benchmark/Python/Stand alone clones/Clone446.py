def fit(self, X, y, n_jobs = 1) :
	self = super(LinearRegression, self).fit(X, y, n_jobs)
	sse = np.sum((self.predict(X) - y) ** 2, axis = 0) / float(X.shape [0] - X.shape [1])
	se = np.array([
	np.sqrt(np.diagonal(sse [i] * np.linalg.inv(np.dot(X.T, X)))) for i in range(sse.shape [0])
	])
	self.t = self.coef_ / se
	self.p = 2 * (1 - stats.t.cdf(np.abs(self.t), y.shape [0] - X.shape [1]))
	return self


def fit(self, x, y) :
	self = super(LinearRegression, self).fit(x, y)
	n, k = x.shape
	yHat = np.matrix(self.predict(x)).T
	x = np.hstack((np.ones((n, 1)), np.matrix(x)))
	y = np.matrix(y).T
	df = float(n - k - 1)
	sse = np.sum(np.square(yHat - y), axis = 0)
	self.sampleVariance = sse / df
	self.sampleVarianceX = x.T * x
	self.covarianceMatrix = sc.linalg.sqrtm(self.sampleVariance [0, 0] * self.sampleVarianceX.I)
	self.se = self.covarianceMatrix.diagonal() [1 :]
	self.betasTStat = np.zeros(len(self.se))
	for i in xrange(len(self.se)) :
		self.betasTStat [i] = self.coef_ [0, i] / self.se [i]
	self.betasPValue = 1 - t.cdf(abs(self.betasTStat), df)

