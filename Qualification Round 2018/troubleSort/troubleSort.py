# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb


# def solve(n, array):
# 	done = False
# 	while not done:
# 		done = True
# 		for i in range(n - 2):
# 			if array[i] >  array[i + 2]:
# 				done = False
# 				array[i], array[i + 1], array[i + 2] = array[i + 2], array[i + 1], array[i]
# 	for i in range(n - 1):
# 		if array[i] > array[i + 1]:
# 			return i
# 	return 'OK'



def solve(n, array):
	even, odd = [], []
	for i in range(n):
		if i % 2 == 0:
			even.append(array[i])
		else:
			odd.append(array[i])
	even.sort()
	odd.sort()

	new_array = []
	for i, j in zip(even, odd):
		new_array.append(i)
		new_array.append(j)
	if n % 2 != 0:
		new_array.append(even[-1])

	for k in range(n - 1):
		if new_array[k] > new_array[k + 1]:
			return k
	return 'OK'	

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t + 1):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print "Case #{}:".format(i), solve(n, array)


assert solve(5, [5, 6, 8, 4, 3]) == 'OK'
assert solve(3, [8, 9, 7]) == 1
assert solve(10, [7, 8, 9, 9, 9, 9, 9, 9, 9, 8]) == 2
assert solve(5, [5, 6, 6, 4, 3]) == 'OK'
assert solve(5, [5, 6, 8, 4, 3]) == 'OK'
assert solve(6, [7, 9, 8, 4, 5, 3]) == 0
assert solve(5, [5, 6, 8, 4, 3]) == 'OK'
assert solve(10, [7, 8, 9, 9, 9, 9, 9, 9, 9, 8]) == 2
assert solve(6, [3, 8, 9, 4, 11, 7]) == 2


