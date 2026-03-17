def touch_value(self, stack, frame) :
	assert self.pushes == 0
	for i in range(self.pops) :
		stack.pop()


def touch_value(self, stack, frame) :
	argc = self.oparg & 0xff
	kwargc = (self.oparg >> 8) & 0xff
	assert kwargc == 0
	if argc > 0 :
		args = stack [- argc :]
		stack [:] = stack [: - argc]
	else :
		args = []
	func = stack.pop()
	assert func in frame.values(), "Uh-oh somebody injected bad function. This does not happen."
	result = func(* args)
	stack.append(result)

