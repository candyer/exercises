class Fraction():
	def __init__(self, nominator, denominator):
		p = self.gcd(nominator, denominator)
		self.nominator = nominator / p
		self.denominator = denominator / p

	def add(self, frac):
		new_nominator = self.nominator * frac.denominator + frac.nominator * self.denominator
		new_denominator = self.denominator * frac.denominator
		return Fraction(new_nominator, new_denominator)

	def __str__(self):
		return '%d / %d' % (self.nominator, self.denominator)

	def gcd(self, a, b):
		for i in range(a,0,-1):
			if a % i == 0 and b % i == 0:
				return i

a = Fraction(3, 5)
print a     #3/5
b = Fraction(2, 5)
c = b.add(a)
print c   #1/1
print c.nominator, '/', c.denominator   #1/1
