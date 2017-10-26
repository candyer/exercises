# https://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709

def blocking(a, b, c, d, blocked):
	bad = [[a, b, c, d], [c, d, a, b]]
	for sub in bad:
		if sub in blocked:
			return False
	return True

def f(dp, i, j, blocked):
	res = 0
	if i >= 1 and blocking(i, j, i - 1, j, blocked):
		res += dp[i - 1][j]
	if j >= 1 and blocking(i, j, i, j - 1, blocked):
		res += dp[i][j - 1]
	return res

def avoid_roads(width, height, blocked):
	width += 1
	height += 1
	dp = [[0 for j in range(width)]for i in range(height)]
	dp[0][0] = 1
	for i in range(height):
		for j in range(width):
			if i != 0 or j != 0:
				dp[i][j] = f(dp, i, j, blocked)
	return dp[-1][-1]

assert avoid_roads(6, 6, [[0,0,0,1],[6,6,5,6]]) == 252
assert avoid_roads(1, 1, [[]]) == 2
assert avoid_roads(35, 31, [[]]) == 6406484391866534976
assert avoid_roads(2,2,[[0,0,1,0],[1,2,2,2],[1,1,2,1]]) == 0

