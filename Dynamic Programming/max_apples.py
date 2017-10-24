# A table composed of N x M cells, each having a certain quantity of apples, is given. 
# You start from the upper-left corner. At each step you can go down or right one cell. 
# Find the maximum number of apples you can collect.

def max_apples(grid):
	rows = len(grid)
	cols = len(grid[0])
	if rows == 0 or cols == 0:	return 0 
	dp = grid
 
	for r in range(rows):
		for c in range(cols):
			if r == 0 and c != 0:
				dp[r][c] += dp[r][c - 1]
				 
			elif r != 0 and c == 0:
				dp[r][c] += dp[r - 1][c]
 
			elif r != 0 and c != 0:
				dp[r][c] += max(dp[r-1][c], dp[r][c-1])

	return dp[rows - 1][cols - 1]
	 
assert max_apples([[1, 2, 3, 4],[1, 7, 1, 6],[2, 9, 5, 90]]) == 114
assert max_apples([[1],[2]]) == 3
assert max_apples([[]]) == 0
assert max_apples([[],[],[]]) == 0
assert max_apples([[1, 2, 3], [3, 2, 1], [4, 7, 1], [2, 3, 6]]) == 24


