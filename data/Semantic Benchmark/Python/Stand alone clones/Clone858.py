def viterbi(transition_probabilities, conditional_probabilities) :
	num_samples = conditional_probabilities.shape [1]
	num_states = transition_probabilities.shape [0]
	c = np.zeros(num_samples)
	viterbi = np.zeros((num_states, num_samples))
	best_path_table = np.zeros((num_states, num_samples))
	best_path = np.zeros(num_samples).astype(np.int32)
	viterbi [:, 0] = conditional_probabilities [:, 0]
	c [0] = 1.0 / np.sum(viterbi [:, 0])
	viterbi [:, 0] = c [0] * viterbi [:, 0]
	for t in range(1, num_samples) :
		for s in range(0, num_states) :
			trans_p = viterbi [:, t - 1] * transition_probabilities [:, s]
			best_path_table [s, t], viterbi [s, t] = max(enumerate(trans_p), key = operator.itemgetter(1))
			viterbi [s, t] = viterbi [s, t] * conditional_probabilities [s] [t]
		c [t] = 1.0 / np.sum(viterbi [:, t])
		viterbi [:, t] = c [t] * viterbi [:, t]
	best_path [num_samples - 1] = viterbi [:, num_samples - 1].argmax()
	for t in range(num_samples - 1, 0, - 1) :
		best_path [t - 1] = best_path_table [best_path [t], t]
	return best_path


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

