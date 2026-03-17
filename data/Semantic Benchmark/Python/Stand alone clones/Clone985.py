def merge_lists(h1, h2) :
	if h1 is None :
		return h2
	if h2 is None :
		return h1
	if (h1.value < h2.value) :
		h1.next = merge_lists(h1.next, h2)
		return h1
	else :
		h2.next = merge_lists(h2.next, h1)
		return h2


def merge_lists(head1, head2) :
	if head1 is None :
		return head2
	if head2 is None :
		return head1
	s = t = node()
	while not (head1 is None or head2 is None) :
		if head1.value < head2.value :
			c = head1
			head1 = head1.next
		else :
			c = head2
			head2 = head2.next
		t.next = c
		t = t.next
	t.next = head1 or head2
	return s.next

