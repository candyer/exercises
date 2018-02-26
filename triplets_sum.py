
# given a list of numbers, return how many different combinations of (i, j, k) 
# fits the following condition:
# nums[i] + nums[j] + nums[k] < target number

# assume (i, j, k), (j, k, i), (k, j, i)... are the same


# complexity O(n**2)
def solve(nums, target):
	nums.sort()
	n = len(nums)
	res = 0
	for i in range(n - 2):
		j = i + 1
		k = n - 1
		while j < k:
			if nums[i] + nums[j] + nums[k] >= target:
				k -= 1
			else:
				res += (k - j)
				j += 1
	return res

assert solve([2, 4, 3, 6, 10, 12], 20) == 12
assert solve([2, 4, 3], 20) == 1
assert solve([2, 4, 3, 7], 20) == 4


