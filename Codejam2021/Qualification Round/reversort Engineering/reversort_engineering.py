# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7

# Limits:
# 1 <= T <= 100.
# 1 <= C <= 1000.
# Test Set 1: 2 <= N <= 7.
# Test Set 2: 2 <= N <= 100.

###########################################
############### test set 1 ################
###########################################
from itertools import permutations

def cost(n, arr):
	res = 0
	for i in range(n - 1):
		mini = min(arr[i:])
		j = arr.index(mini) + 1
		arr[i: j] = reversed(arr[i: j])
		res += j - i
	return res

def solve(n, c):
	mini, maxi = n - 1, sum(range(2, n + 1))
	if c < mini or c > maxi:
		return 'IMPOSSIBLE'
	for arr in permutations(range(1, n + 1), n):
		if cost(n, list(arr)) == c:
			return ' '.join(map(str, arr))

if __name__ == '__main__':
	T = int(input())
	for t in range(1, T + 1):
		n, c  = map(int, input().split())
		print('Case #{}:'.format(t), solve(n, c))


###########################################
############### test set 2 ################
###########################################

def solve(n, c):
	mini, maxi = n - 1, sum(range(2, n + 1))
	if c < mini or c > maxi:
		return 'IMPOSSIBLE'
	pos = list(range(n))
	cost = [1] * (n - 1)
	c = c - n + 1
	for i in range(n - 1):		
		cur = min(c, n - i - 1)
		cost[i] += cur
		pos[i: i + cost[i]] = reversed(pos[i: i + cost[i]])
		c -= cur
	res = [0] * n
	for num, i in zip(range(1, n + 1), pos):
		res[i] = num
	return ' '.join(map(str, res))

if __name__ == '__main__':
	T = int(input())
	for t in range(1, T + 1):
		n, c  = map(int, input().split())
		print('Case #{}:'.format(t), solve(n, c))


assert(solve(4, 6) == '4 3 2 1')
assert(solve(2, 1) == '1 2')
assert(solve(7, 12) == '7 6 5 4 3 2 1')
assert(solve(7, 2) == 'IMPOSSIBLE')
assert(solve(2, 1000) == 'IMPOSSIBLE')
