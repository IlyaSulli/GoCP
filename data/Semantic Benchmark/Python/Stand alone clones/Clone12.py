def topic_prob_extractor(hdp = None, topn = None) :
	topic_list = hdp.show_topics(topics = - 1, topn = topn)
	topics = [int(x.split(':') [0].split(' ') [1]) for x in topic_list]
	split_list = [x.split(' ') for x in topic_list]
	weights = []
	for lst in split_list :
		sub_list = []
		for entry in lst :
			if '*' in entry :
				sub_list.append(float(entry.split('*') [0]))
		weights.append(np.asarray(sub_list))
	sums = [np.sum(x) for x in weights]
	return pd.DataFrame({'topic_id' : topics, 'weight' : sums})


def topic_prob_extractor(gensim_hdp, t = - 1, w = 25, isSorted = True) :
	shown_topics = gensim_hdp.show_topics(num_topics = t, num_words = w, formatted = False)
	topics_nos = [x [0] for x in shown_topics]
	weights = [sum([item [1] for item in shown_topics [topicN] [1]]) for topicN in topics_nos]
	if (isSorted) :
		return pd.DataFrame({'topic_id' : topics_nos, 'weight' : weights}).sort_values(by = "weight", ascending = False);
	else :
		return pd.DataFrame({'topic_id' : topics_nos, 'weight' : weights});

