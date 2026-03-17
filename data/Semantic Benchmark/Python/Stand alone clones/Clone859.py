def viterbi(y, A, B, Pi = None) :
	K = A.shape [0]
	Pi = Pi if Pi is not None else np.full(K, 1 / K)
	T = len(y)
	T1 = np.empty((K, T), 'd')
	T2 = np.empty((K, T), 'B')
	T1 [:, 0] = Pi * B [:, y [0]]
	T2 [:, 0] = 0
	for i in range(1, T) :
		T1 [:, i] = np.max(T1 [:, i - 1] * A.T * B [np.newaxis, :, y [i]].T, 1)
		T2 [:, i] = np.argmax(T1 [:, i - 1] * A.T, 1)
	x = np.empty(T, 'B')
	x [- 1] = np.argmax(T1 [:, T - 1])
	for i in reversed(range(1, T)) :
		x [i - 1] = T2 [x [i], i]
	return x, T1, T2


def viterbi(self, observations) :
	nSamples = len(observations [0])
	nStates = self.transition.shape [0]
	c = np.zeros(nSamples)
	viterbi = np.zeros((nStates, nSamples))
	psi = np.zeros((nStates, nSamples))
	best_path = np.zeros(nSamples);
	viterbi [:, 0] = self.priors.T * self.emission [:, observations(0)]
	c [0] = 1.0 / np.sum(viterbi [:, 0])
	viterbi [:, 0] = c [0] * viterbi [:, 0]
	psi [0] = 0;
	for t in range(1, nSamples) :
		for s in range(0, nStates) :
			trans_p = viterbi [:, t - 1] * self.transition [:, s]
			psi [s, t], viterbi [s, t] = max(enumerate(trans_p), key = operator.itemgetter(1))
			viterbi [s, t] = viterbi [s, t] * self.emission [s, observations(t)]
		c [t] = 1.0 / np.sum(viterbi [:, t])
		viterbi [:, t] = c [t] * viterbi [:, t]
	best_path [nSamples - 1] = viterbi [:, nSamples - 1].argmax()
	for t in range(nSamples - 1, 0, - 1) :
		best_path [t - 1] = psi [best_path [t], t]
	return best_path

