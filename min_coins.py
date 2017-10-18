
# Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. 
# Find the minimum number of coins the sum of which is S (we can use as many coins of one type as 
# we want), or return -1 that it's not possible to select coins in such a way that they sum up to S.

def solve(coins, target):
	dp = [-1] * (target + 1)
	dp[0] = 0
	for i in range(1, target + 1):
		for val in coins:
			if val <= i:
				if dp[i - val] != -1 and (dp[i] > dp[i - val] or dp[i] == -1):
					dp[i] = dp[i - val] + 1
	return dp[target]

print solve([2,3,5], 12) #3
print solve([2,4,6], 11) #-1
print solve([5,3,1], 11) #3
print solve([7,2,3,6], 13) #2
