# https://code.google.com/codejam/contest/12224486/dashboard#s=p0&a=0

def solve(f, s, tickets):
	d = {}
	res = 0
	for a, b in tickets:
		if not a in d:
			d[a] = set([b])
		else:
			d[a].add(b)

		if not b in d:
			d[b] = set([a])
		else:
			d[b].add(a)

	res = 0
	for val in d.values():
		res = max(res, len(val))
	return res

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1,T+1):
		f, s = map(int,raw_input().split())
		tickets = []
		for i in range(f):
			seat = map(int,raw_input().split())
			tickets.append(seat)
		print "Case #{}:".format(t), solve(f,s,seats)


# print solve(2, 3, [[1, 2], [1, 2]]) #1
# print solve(3, 3, [[1, 2], [2, 3], [2, 2]]) #3
# print solve(3, 3, [[1, 1], [2, 2], [1, 2]]) #2

