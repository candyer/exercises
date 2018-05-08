# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard


##################
### solution 1 ###
##################

# def f(grid, alphabets):
# 	stack = [(0, '')]
# 	while stack:
# 		pos, prefix = stack.pop()
# 		if pos >= len(alphabets):
# 			if prefix in grid: continue
# 			return prefix
# 		for letter in alphabets[pos]:
# 			stack.append((pos + 1, prefix + letter))
# 	return '-'


# from collections import defaultdict 
# def solve(n, l, grid):
# 	alphabets = defaultdict(set)
# 	for j in range(l):
# 		for i in range(n):
# 			alphabets[j].add(grid[i][j])
# 	return f(grid, alphabets)



# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for i in range(1, t + 1):
# 		n, l = map(int, raw_input().split())
# 		grid = []
# 		for j in range(n):
# 			tmp = raw_input()
# 			grid.append(tmp)
# 		print "Case #{}: {}".format(i, solve(n, l, grid))





##################
### solution 2 ###
##################

def f(grid, d, pos = 0, prefix = ''):
	if pos >= len(d):
		return None if prefix in grid else prefix
	for c in d[pos]:
		word = f(grid, d, pos + 1, prefix + c)
		if word: return word


from collections import defaultdict 
def solve(n, l, grid):
	alphabets = defaultdict(set)
	for j in range(l):
		for i in range(n):
			alphabets[j].add(grid[i][j])
	word = f(grid, alphabets)
	if word:
		return word
	return '-'

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1, t + 1):
		n, l = map(int, raw_input().split())
		grid = []
		for j in range(n):
			tmp = raw_input()
			grid.append(tmp)
		print "Case #{}: {}".format(i, solve(n, l, grid))

print solve(4, 2, ['WW','AA','SS','DD'])

print solve(5, 7, ['HELPIAM',
  		 'TRAPPED',
  		 'INSIDEA',
  		 'CODEJAM',
  		 'FACTORY'])

assert solve(4, 2, ['AA','AB','BA','BB']) == '-'



