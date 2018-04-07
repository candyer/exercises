# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/


def f1(p):
	current_damage = 1
	total = 0
	for instruction in p:
		if instruction == 'S':
			total += current_damage
		else:
			current_damage *= 2
	return total

def f2(p, n):
	flag = False
	for i in range(n - 1, 0, -1):
		if p[i - 1] == 'C' and p[i] == 'S':
			p[i - 1], p[i] = p[i], p[i - 1]
			flag = True
			break
	return p, flag

def solve(d, p):
	# '''
	# 1 <= T <= 100.
	# 1 <= D <= 109.
	# 2 <= length of P <= 30.
	# Every character in P is either C or S.
	# Time limit: 20 seconds per test set.
	# Memory limit: 1GB.
	# '''
	if f1(p) <= d:
		return 0
	n = len(p)
	res = 0
	while True:
		p, flag = f2(p, n)
		if not flag:
			return 'IMPOSSIBLE'
		elif f1(p) > d:
			res += 1
		elif f1(p) <= d:
			return res + 1

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		d, p = raw_input().split()
		d = int(d)
		p = list(p)
		print "Case #{}:".format(i), solve(d, p)

# assert solve(1, ['C', 'S']) == 1
# assert solve(2, ['C', 'S']) == 0
# assert solve(1, ['S', 'S']) == 'IMPOSSIBLE'
# assert solve(6, ['S', 'C', 'C', 'S', 'S', 'C']) == 2
# assert solve(2, ['C', 'C']) == 0
# assert solve(3, ['C', 'S', 'C', 'S', 'S']) == 5
# print solve(3, ['S', 'C', 'C', 'S', 'S', 'C'])


