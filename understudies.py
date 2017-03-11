# https://code.google.com/codejam/contest/12224486/dashboard#s=p1&a=1

def solve(n, array):
	array.sort()
	res = 1
	for i in range(n):
		res *= (1 - array[i] * array[2 * n - i - 1])
	return "{0:.8f}".format(res)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1,T+1):
		n = int(raw_input())
		array = map(float,raw_input().split())
		print "Case #{}:".format(t), solve(n, array)


# print solve(2, [0.25, 0.5, 0.5, 0.25]) #0.76562500
# print solve(3, [0.0, 0.0, 0.0, 0.0009, 0.0013, 0.1776]) #1.00000000
# print solve(1, [1.0, 0.1234]) #0.87660000
