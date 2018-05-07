# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard


def f(grid, alphabets):
	stack = [(0, '')]
	while stack:
		pos, prefix = stack.pop()
		if pos >= len(alphabets):
			if prefix in grid: continue
			return prefix
		for letter in alphabets[pos]:
			stack.append((pos + 1, prefix + letter))
	return '-'


from collections import defaultdict 
def solve(n, l, grid):
	alphabets = defaultdict(set)
	for j in range(l):
		for i in range(n):
			alphabets[j].add(grid[i][j])
	return f(grid, alphabets)



if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1, t + 1):
		n, l = map(int, raw_input().split())
		grid = []
		for j in range(n):
			tmp = raw_input()
			grid.append(tmp)
		print "Case #{}: {}".format(i, solve(n, l, grid))



