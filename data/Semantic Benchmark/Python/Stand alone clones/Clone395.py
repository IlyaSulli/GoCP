def corr(data1, data2) :
	"data1 & data2 should be numpy arrays."
	mean1 = data1.mean()
	mean2 = data2.mean()
	std1 = data1.std()
	std2 = data2.std()
	corr = ((data1 * data2).mean() - mean1 * mean2) / (std1 * std2)
	return corr


def corr(data1, data2) :
	M = data1.size
	sum1 = 0.
	sum2 = 0.
	for i in range(M) :
		sum1 += data1 [i]
		sum2 += data2 [i]
	mean1 = sum1 / M
	mean2 = sum2 / M
	var_sum1 = 0.
	var_sum2 = 0.
	cross_sum = 0.
	for i in range(M) :
		var_sum1 += (data1 [i] - mean1) ** 2
		var_sum2 += (data2 [i] - mean2) ** 2
		cross_sum += (data1 [i] * data2 [i])
	std1 = (var_sum1 / M) **.5
	std2 = (var_sum2 / M) **.5
	cross_mean = cross_sum / M
	return (cross_mean - mean1 * mean2) / (std1 * std2)

