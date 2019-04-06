# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

def solve(n):
	digits = map(int, list(str(n)))
	length = len(digits)
	res = 0
	for i, num in enumerate(digits):
		if num == 4:
			res += 1 * pow(10, length - i - 1)
	return '{} {}'.format(res, n - res)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		n = int(raw_input())
		print "Case #{}:".format(t), solve(n)

assert solve(4) == '1 3'
assert solve(940) == '10 930'
assert solve(4444) == '1111 3333'
assert solve(9401) == '100 9301'
assert solve(9444444444) == '111111111 9333333333'

