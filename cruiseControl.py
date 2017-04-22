# https://code.google.com/codejam/contest/8294486/dashboard#s=p0

def cruiseControl(d, n, array):
	time = 0
	for k, s in array:
		tmp = (d - k) / float(s)
		time = max(time, tmp)
	return "{0:.6f}".format(d / time) 

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		d, n = map(int, raw_input().split())
		array = []
		for j in range(n):
			tmp = map(int, raw_input().split())
			array.append(tmp)
		print "Case #{}:".format(i), cruiseControl(d, n, array)
