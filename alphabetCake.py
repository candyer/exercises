# https://code.google.com/codejam/contest/5304486/dashboard#s=p0&a=0

def alphabetCake(r, c, grid):
	for i in range(r):
		for j in range(c - 1):
			if grid[i][j] != '?' and grid[i][j + 1] == '?':
				grid[i][j + 1] = grid[i][j]

	for i in range(r):
		for j in range(c - 1, 0, -1):
			if grid[i][j] != '?' and grid[i][j - 1] == '?':
				grid[i][j - 1] = grid[i][j]

	for k in range(r - 1):
		if grid[k][0] != '?' and grid[k + 1][0] == '?':
			grid[k + 1] = grid[k]

	for l in range(r - 1, 0, -1):
		if grid[l][0] != '?' and grid[l - 1][0] == '?':
			grid[l - 1] = grid[l]

	res = []
	for i in range(r):
		res.append(''.join(grid[i]))
	return '\n'.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		r, c = map(int, raw_input().split())
		grid = []
		for j in range(r):
			tmp = list(raw_input())
			grid.append(tmp)
		print "Case #{}:{}".format(i, '\n'), alphabetCake(r, c, grid)


# print alphabetCake(3, 3, [['?', '?', '?'], 
# 			   ['?', 'A', '?'],
# 			   ['?', '?', '?']]) 

#'AAA
# AAA
# AAA'

# print alphabetCake(3, 3, [['M', '?', 'D'], 
# 			   ['?', '?', '?'],
# 			   ['B', '?', 'C']])

# 'MMD
# MMD
# BBC'

# print alphabetCake(3, 3, [['G', '?', '?'], 
# 			   ['?', 'C', '?'],
# 			   ['?', '?', 'J']])

# 'GGG
# CCC
# JJJ'

# print alphabetCake(3, 4, [['C', 'O', 'D', 'E'], 
# 			   ['?', '?', '?', '?'],
# 			   ['?', 'J', 'A', 'M']])

# 'CODE
# CODE
# JJAM'

# print alphabetCake(2, 2, [['C', 'A'], 
# 			   ['K', 'E']])

# 'CA
# KE'

