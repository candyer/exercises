# https://leetcode.com/problems/longest-palindromic-subsequence/description/
# Given a string s, find the longest palindromic subsequence's length in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:  Input:"bbbab"  Output:4
# One possible longest palindromic subsequence is "bbbb".

# Example 2:  Input:"cbbd"   Output:2
# One possible longest palindromic subsequence is "bb".

def longest_palindrome(s):
	n = len(s)
	if n == 0: return 0
	dp = [[0 for i in range(n)] for j in range(n)]
	for i in range(n): #this for loop means all the substring of length 1 can form a palindrome with at most length 1
		dp[i][i] = 1

	for j in range(2, n + 1): # j is length of each substring
		for k in range(n - j + 1): # n - j + 1 means the last substring in this loop start at 'n - j + 1'
			l = j + k - 1 
			if j == 2 and s[k] == s[l]:
				dp[k][l] = 2 # means two adjacent letters are identical
			else:
				if s[k] == s[l]:
					dp[k][l] = dp[k + 1][l - 1] + 2
				else:
					dp[k][l] = max(dp[k + 1][l], dp[k][l - 1])
	return dp[0][-1]

assert longest_palindrome('') == 0
assert longest_palindrome('z') == 1
assert longest_palindrome('cbba') == 2
assert longest_palindrome('bbbab') == 4
assert longest_palindrome('bbabb') == 5
assert longest_palindrome('abcghjcbaaaa') == 7
assert longest_palindrome('kjhgfdsasdfghj') == 13
