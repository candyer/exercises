
# Given a sequence of N numbers: A[1], A[2], ..., A[N].
# Find the length of the longest non-decreasing sequence.

def longest_non_decs_seq(array):
	if array == []: return 0
	n = len(array)
	dp = [1] * n	
	for i in range(1, n):
		for j in range(i):
			if array[i] >= array[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	return max(dp)

assert longest_non_decs_seq([1,4,2,7,2,5,6]) == 5
assert longest_non_decs_seq([5,3,4,8,4,6,7]) == 5
assert longest_non_decs_seq([]) == 0
assert longest_non_decs_seq([7]) == 1
assert longest_non_decs_seq([10, 22, 9, 33, 21, 50, 41]) == 4
