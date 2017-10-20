# https://community.topcoder.com/stat?c=problem_statement&pm=2402

# The old song declares "Go ahead and hate your neighbor", and the residents of Onetinville have taken 
# those words to heart. Every resident hates his next-door neighbors on both sides. Nobody is willing 
# to live farther away from the town's well than his neighbors, so the town has been arranged in a big 
# circle around the well. Unfortunately, the town's well is in disrepair and needs to be restored. 
# You have been hired to collect donations for the Save Our Well fund.

# Each of the town's residents is willing to donate a certain amount, as specified in the int[] donations, 
# which is listed in clockwise order around the well. However, nobody is willing to contribute to a fund 
# to which his neighbor has also contributed. Next-door neighbors are always listed consecutively in donations, 
# except that the first and last entries in donations are also for next-door neighbors. You must calculate 
# and return the maximum amount of donations that can be collected.

# Constraints
# - donations contains between 2 and 40 elements, inclusive.
# - Each element in donations is between 1 and 1000, inclusive.

def max_donation(array):
	n = len(array)
	if n == 0: return 0
	elif n == 1: return array[0]
	first = array[:-1]
	second = array[1:]
	for i in range(n - 1):
		for j in range(i + 2, n - 1):
			first[j] = max(first[j], first[i] + array[j])
			second[j] = max(second[j], second[i] + array[j + 1])
	if n >= 3:
		return max(first[-1], first[-2], second[-1], second[-2])
	return max(first[-1], second[-1])


def max_donation1(array):
	n = len(array)
	if n == 1: return array[0]
	first = res1 = second = res2 = 0
	for i in range(n - 1):
		first, res1 = res1, max(res1, first + array[i])
		second, res2 = res2, max(res2, second + array[i + 1])
	return max(res1, res2)

# assert max_donation([1]) == 1
# assert max_donation([1,2,3]) == 3
# assert max_donation([3,2,1,8,7]) == 11
# assert max_donation([14, 9, 6, 1, 3, 4, 2, 11, 8, 9]) == 35
# assert max_donation([15, 2, 2, 11, 12, 12, 4, 15, 7, 7]) == 53
# assert max_donation([10, 4, 13, 4, 14, 5, 10, 13, 2, 9]) == 50
# assert max_donation([13, 7, 2, 13, 14, 12, 4, 7, 6, 3]) == 45
# assert max_donation1([1, 10, 1, 1, 9]) == 19
# assert max_donation([10, 3, 2, 5, 7, 8]) == 19
# assert max_donation([1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ]) == 16
# assert max_donation([7, 7, 7, 7, 7, 7, 7]) == 21
# assert max_donation([11, 15]) == 15
# assert max_donation([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,  
					# 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
					# 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72]) == 2926
