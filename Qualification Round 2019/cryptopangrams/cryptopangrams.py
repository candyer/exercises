# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

from fractions import gcd
def solve(n, l, array):
	i = 0
	primes = [0] * (l + 1)
	while i < l - 1:
		if array[i] != array[i + 1]:
			primes[i + 1] = (gcd(array[i], array[i + 1]))
		i += 1
	j = 0
	while j < l - 1:
		k = j
		while k >= 0 and primes[k] == 0 and primes[k + 1]:
			primes[k] = array[k] / primes[k + 1]
			k -= 1
		j += 1
	m = 0
	while m < l + 1:
		if primes[m - 1] != 0 and primes[m] == 0:
			primes[m] = array[m - 1] / primes[m - 1]
		m += 1

	d = {}
	for num, letter in zip(sorted(list(set(primes))), range(65, 91)):
		d[num] =  chr(letter)

	res = []
	for c in primes:
		res.append(d[c])
	return ''.join(res) 


if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		n, l = map(int,raw_input().split())
		array = map(int,raw_input().split())
		print "Case #{}:".format(t), solve(n, l, array)


assert solve(10403, 51, 
	[5329, 5329, 5329, 5329, 5329, 5329, 1679, 299, 793, 4819, 2291, 203, 259, 185, 335, 3551, 4717, 
	4183, 799, 901, 5141, 3007, 2449, 3397, 3397, 3397, 3397, 3397, 3397, 4661, 4189, 3763, 4399, 1079, 
	871, 4891, 1679, 299, 533, 123, 309, 10403, 1111, 583, 1007, 1007, 1007, 361, 361, 361, 361]) == 'TTTTTTTHEQUICKBROWNFOXJUMUMUMUPSOVERTHELAZYDOGOGGGGG'
assert solve(10403, 41, 
	[1679, 299, 793, 4819, 2291, 203, 259, 185, 335, 3551, 4717, 4183, 799, 901, 5141, 3007, 2449, 
	3397, 3397, 3397, 3397, 3397, 3397, 4661, 4189, 3763, 4399, 1079, 871, 4891, 1679, 299, 
	533, 123, 309, 10403, 1111, 583, 1007, 1007, 1007]) == 'THEQUICKBROWNFOXJUMUMUMUPSOVERTHELAZYDOGOG'
assert solve(10403, 36, [1679, 299, 793, 4819, 2291, 203, 259, 185, 335, 3551, 4717, 4183, 799, 901, 5141, 3007, 2449, 3397, 2537, 
	4189, 3763, 4399, 1079, 871, 4891, 1679, 299, 533, 123, 309, 10403, 1111, 583, 1007, 1007, 1007]) == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOGOG'
assert solve(103, 31, 
  [217, 1891, 4819, 2291, 2987, 3811, 1739, 2491, 4717, 445, 65, 1079, 8383, 5353, 901, 187, 649, 
  1003, 697, 3239, 7663, 291, 123, 779, 1007, 3551, 1943, 2117, 1679, 989, 3053]) == 'CJQUIZKNOWBEVYOFDPFLUXALGORITHMS'
assert solve(10000, 25, 
  [3292937, 175597, 18779, 50429, 375469, 1651121, 2102, 3722, 2376497, 611683, 489059, 2328901, 3150061, 
  829981, 421301, 76409, 38477, 291931, 730241, 959821, 1664197, 3057407, 4267589, 4729181, 5335543]) == 'SUBDERMATOGLYPHICFJKNQVWXZ'

