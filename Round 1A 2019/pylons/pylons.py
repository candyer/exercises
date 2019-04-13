# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03


def is_answer_valid(r, c, grid):
	d = {}
	for i in range(r):
		for j in range(c):
			d[grid[i][j]] = [i + 1, j + 1]
	res = []
	for i in range(1, r * c):
		x1, y1 = d[i]
		x2, y2 = d[i + 1]
		if x1 == x2 or y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
			return False
	return True

def generate_steps(r, c, grid):
	d = {}
	for i in range(r):
		for j in range(c):
			d[grid[i][j]] = '{} {}'.format(i + 1, j + 1)
	res = []
	for i in range(1, r * c + 1):
		res.append(d[i])
	return '\n'.join(res)

def geneate_3_rows(c, start, end):
	x = range(start, end - 7, 3) + [0] * 2
	y = [0] * 2 + range(start + 1, end - 6, 3)
	z = range(start + 2, end - 5, 3) + [0] * 2
	grid = [x, y, z]
	start += (c - 2) * 3
	xx = [0, 1, 2]
	yy = [c - 2, 0, c - 2]
	for _ in range(2):
		for i in range(3):
			grid[xx[i]][yy[i]] = start
			yy[i] += 1
			start += 1  
	return grid

def generate_2_rows(c, start, end):
	x = range(start, end , 2)
	y = range(start + 1, end + 1 , 2)
	grid = [x[-2:] + x[:-2], y]
	return grid


def solve(r, c):
	if r == 1 or c == 1 or r + c <= 6:
		return 'IMPOSSIBLE'
	flag = False
	if r > c:
		r, c = c, r
		flag = True
	grid = []
	if r % 3 == 0:
		start = 1
		end = c * 3
		for _ in range(r / 3):
			grid.extend(geneate_3_rows(c, start, end))
			start = end + 1
			end += c * 3
	elif r % 2 == 0:
		start = 1
		end = c * 2
		for i in range(r / 2):
			grid.extend(generate_2_rows(c, start, end))
			start = end + 1
			end += c * 2

	elif r % 2 != 0:
		start = 1
		end = c * 3
		grid.extend(geneate_3_rows(c, start, end))
		num_rows_remaining = r - 3
		start = end + 1
		end += c * 2

		for i in range(num_rows_remaining / 2):
			grid.extend(generate_2_rows(c, start, end))
			start = end + 1
			end += c * 2        
	if r == c == 4:
		grid = [[1,13,5,10],[4,7,2,14],[12,15,9,6],[8,3,11,16]]
	if flag:
		res = [[0 for j in range(r)] for i in range(c)]
		for i in range(c):
			for j in range(r):
				res[i][j] = grid[j][i]
		grid = res
		assert is_answer_valid(c, r, grid)
		print 'POSSIBLE'
		return generate_steps(c, r, grid)
	else:
		assert is_answer_valid(r, c, grid)
		print 'POSSIBLE'
		return generate_steps(r, c, grid)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		r, c = map(int,raw_input().split())
		print "Case #{}:".format(t), solve(r, c)


