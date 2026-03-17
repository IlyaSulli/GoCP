def __str__(self) :
	return textwrap.dedent('''\
	Car Type
	mpg: %.1f
	hp: %.2f
	pc: %i
	unit cost: $%.2f
	price: $%.2f''' % (self.mpg, self.hp, self.pc, self.cost, self.price))


def __str__(self) :
	dd = (
	("Car Type     %s", ''),
	("  mpg:       %.1f", self.mpg),
	("  hp:        %.2f", self.hp),
	("  pc:        %i", self.pc),
	("  unit cost: $%.2f", self.cost),
	("  price:     $%.2f", self.price),
	)
	fmt = ''.join("%s\n" % t [0] for t in dd)
	return fmt % tuple(t [1] for t in dd)

