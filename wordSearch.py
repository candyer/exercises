# https://code.google.com/codejam/contest/12224486/dashboard#s=p2&a=2

# small input
def solve(d, n):
	if n == 0: 
		return '//'
	a = 'I/OI/OI/OI/OI/OI/OI/OI/OI/OI/OI/OI/O'
	b = 'OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO'
	res = []
	while n:
		s = n / 12
		for _ in range(s):
			res.append(a)
			res.append(b)
		count = n % 12
		if count > 0:
			res.append('I/O' *  count + 'O' * (36 - count * 3))
			break
	return '\n'.join(res)




# large input
def solve(d, n):
	a = [
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O'],
		['I','/','O','/','I','/','O','/','I','/','O','/','I','/','O']
		]

	b = 287 - n
	count = b / 21
	tmp = b % 21
	while count: 
		for i in range(1, 15, 2):
			a[count][i] = "O"
		count -= 1
	
	while tmp > 14:
		for i in range(1, 15, 2):
			a[b / 21 + 1][i] = "O"	
			tmp -= 3	
			if tmp < 14:
				break

	if 0 < tmp <= 14:
		for j in range(1, 15, 2):
			if tmp <= 0: break
			a[0][j] = "O"
			tmp -= 1
			
		for k in range(1, 15, 2):
			if tmp <= 0: break
			a[14][k] = "O"
			tmp -= 1
			
	res = []
	for row in a:
		res.append(''.join(row))
	return '\n'.join(res)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1,T+1):
		d, n = map(int,raw_input().split())
		print "Case #{}: {}".format(t, "\n"), solve(d, n)

