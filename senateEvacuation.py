
def solve(n, array):
	parties = map(lambda i: chr(65 + i), range(n))
	res = []
	while True:
		maxi = max(array)
		if maxi == 0:
			return ' '.join(res)
		idx = filter(lambda i: array[i] == maxi, range(n))

		if len(idx) == 2:
			res.append(parties[idx[0]] + parties[idx[1]])
			array[idx[0]] -= 1
			array[idx[1]] -= 1
		else:
			res.append(parties[idx[0]])
			array[idx[0]] -= 1

# if __name__ == '__main__':
# 	T = int(raw_input())
# 	for t in range(1,T+1):
# 		n = int(raw_input())
# 		array = map(int,raw_input().split())
# 		print "Case #{}:".format(t), solve(n, array)


print solve(2, [2, 2]) == 'AB AB'
print solve(3, [3, 2, 2]) == 'A A BC A BC'
print solve(3, [1, 1, 2]) == 'C A BC'
print solve(3, [2, 3, 1]) == 'B AB A BC'
