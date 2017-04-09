# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

#############################################################
# for small input (1 ≤ N ≤ 1000), too slow for large input. #
#############################################################

def isNumberTidy(n):
	s = list(str(n))
	if s != sorted(s): return False
	return 'True'

def tidyNumbers(n):
	if isNumberTidy(n): return n
	i = 1
	while True:
		if isNumberTidy(n-i):
			return n - i
		i += 1

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n = int(raw_input())
		print "Case #{}:".format(i), tidyNumbers(n)

# print tidyNumbers(11111) #11111
# print tidyNumbers(9987) #8999
# print tidyNumbers(123432) #123399
# print tidyNumbers(123439) #123399
# print tidyNumbers(2233454) #2233449


##################################
# for large input (1 ≤ N ≤ 1018).#
##################################

def isNumberTidy(s):
	if s == [] or s != sorted(s): return False
	return True

def tidyNumbers(n):
	s = list(str(n))
	res = []
	index = 0
	length = len(s)
	for i in range(length - 1):
		if s[i] > s[i+1]:
			index = i + 1
			break
	if index == 0: return n

	while index > 0:
		if s[index] > s[index - 1]:
			res = s[:index - 1] + [str(int(s[index]) - 1)] + ['9'] * (length - index - 1)
			if res[0] == '0': res = res[1:]
		elif s[index] == s[index - 1]:
			res = s[:index + 1] + ['9'] * (length - index - 1)
			if res[0] == '0': res = res[1:]
		elif s[index] < s[index - 1]:
			s[index - 1] = str(int(s[index - 1]) - 1)
			s[index:] = ['9'] * (length - index)
			res = s
		if isNumberTidy(res):
			break
		index -= 1
	if res[0] == '0':
		res = res[1:]
	return ''.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n = int(raw_input())
		print "Case #{}:".format(i), tidyNumbers(n)

# print tidyNumbers(111111111111111110) #99999999999999999
# print tidyNumbers(220232222222222221) #199999999999999999
# print tidyNumbers(568565500917251027) #567999999999999999
# print tidyNumbers(13378801123478899) #13377999999999999


