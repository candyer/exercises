# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

# Limits
# 1 <= T <= 100.
# 2 <= N <= 100.
# 1 <= Li <= N, for all i.
# Li != Lj, for all i != j. all elements in arr are unique. 1 <= arr[i] <= n

def solve(n, arr):
	res = 0
	for i in range(n - 1):
		mini = min(arr[i:])
		j = arr.index(mini) + 1
		arr[i: j] = reversed(arr[i: j])
		res += j - i
	return res

if __name__ == '__main__':
	T = int(input())
	for t in range(1, T + 1):
		n = int(input())
		arr = list(map(int, input().split()))
		print('Case #{}:'.format(t), solve(n, arr))


assert(solve(6, [6, 5, 2, 3, 4, 1]) == 12)
assert(solve(4, [4, 2, 1, 3]) == 6)
assert(solve(2, [1, 2]) == 1)
assert(solve(7, [7, 6, 5, 4, 3, 2, 1]) == 12)
assert(solve(9, [1, 3, 5, 4, 6, 8, 9, 2, 7]) == 23)

