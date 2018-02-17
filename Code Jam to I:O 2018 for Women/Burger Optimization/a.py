
def f(n):
	res = []
	if n % 2 != 0:
		res.append(n / 2)
	for i in range(n / 2 - 1, -1, -1):
		res.append(i)
		res.append(i)
	return res

def solve(k, array):
	array.sort(reverse=True)
	ff = f(k)
	res = 0
	for a, b in zip(array, ff):
		res += (a - b) * (a - b)
	return res

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1,T+1):
		k = int(raw_input())
		array = map(int,raw_input().split())
		print "Case #{}:".format(t), solve(k, array)


		