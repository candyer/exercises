# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30


def f(row_start, row_end, col_start, col_end):
	total = {}
	for j in range(row_start, row_end + 1):
		for k in range(col_start, col_end + 1):	
			total[(j, k)] = False
	return total

def f1(row_start, row_end, col_start, col_end):
	choices = []
	for j in range(row_start, row_end + 1):
		for k in range(col_start, col_end + 1):	
			choices.append((j, k))
	return choices

def f2(total, pos):
	x, y = pos
	flag = True
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if not total[(i, j)]:
				flag = False
				break
		if not flag:
			break
	return flag


import sys
if __name__ == '__main__':	
	t = int(raw_input())
	for _ in range(t):
		a = int(raw_input())
		row_start = 501
		col_start = 501
		row_end = 0
		col_end = 0
		if a == 20:
			row_end = 502
			col_end = 503
		else:
			row_end = 508
			col_end = 518			

		i = 0
		total = f(row_start - 1, row_end + 1, col_start - 1, col_end + 1)
		choices = f1(row_start, row_end, col_start, col_end)

		n = len(choices)
		while i < 1000:
			pos = choices[i % n]
			if f2(total, pos): #no need to choose this pos any more
				choices.pop(i % n)
				n -= 1
			
			x, y = choices[i % n]
			print ' '.join([str(x), str(y)])
			sys.stdout.flush()
			x1, y1 = map(int, raw_input().split())
			total[(x1, y1)] = True
			if x1 == y1 == 0:
				break
			i += 1


			


# print f(500, 503, 500, 504)
# print f1(501, 502, 501, 503)
# total = {(502, 500): True, (501, 500): False, (501, 503): True, (502, 503): True, (500, 502): True, (500, 504): True, (500, 501): True, (503, 504): True, (503, 502): True, (500, 500): True, (500, 503): True, (503, 503): True, (502, 502): True, (503, 500): True, (501, 502): True, (503, 501): True, (502, 501): True, (502, 504): True, (501, 504): True, (501, 501): True}
# choices = [(501, 501), (501, 502), (501, 503), (502, 501), (502, 502), (502, 503)]
# pos = (501, 501)
# pos = (502, 502)
# print f2(total, choices, pos)



