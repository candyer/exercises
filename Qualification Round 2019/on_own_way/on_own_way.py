# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

def solve(n, p):
	res = []
	for move in p:
		if move == 'E':
			res.append('S')
		else:
			res.append('E')
	return ''.join(res)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		n = int(raw_input())
		p = raw_input()
		print "Case #{}:".format(t), solve(n, p)

assert solve(2, 'SE') == 'ES'
assert solve(5, 'EESSSESE') == 'SSEEESES'
assert solve(6, 'SESESESESE') == 'ESESESESES'
assert solve(10, 'ESSSSESESEEEESEESS') == 'SEEEESESESSSSESSEE'