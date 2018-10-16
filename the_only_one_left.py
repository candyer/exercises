

# given an array of integers from 1 to 100, remove all the odd position numbers until there is only one left, which number is it?

#####################
#### brute force ####
#####################
def the_only_one_left(nums):
	while len(nums) > 1:
		tmp = []
		for i, num in enumerate(nums):
			if (i + 1) % 2 == 0:
				tmp.append(num)
		nums = tmp
	return nums[0]

assert the_only_one_left(range(1, 101)) == 64



#####################
## faster solution ##
#####################
# convert 100 into binary, which is bin(100)[2:] = '1100100', 7 digits. we want to find out the number that was on the even position every time, 
# the answer is 2 ** (7 - 1) = 64.
def the_only_one_left(nums):
	return pow(2, len(bin(nums[-1])[2:]) - 1)

assert the_only_one_left(range(1, 101)) == 64



#change the problem a bit: given an array of integers from 1 to n, remove all the odd position numbers until there is only one left, which number is it?
# answer is the maxmum number less than n and is power of 2

def the_only_one_left(n):
	return pow(2, len(bin(n)[2:]) - 1)


assert the_only_one_left(10**9) == 536870912 # 2**29
