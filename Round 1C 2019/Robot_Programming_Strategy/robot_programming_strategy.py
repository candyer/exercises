# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90

def get_moves(programs, idx):
	moves = set()
	for program in programs:
		moves.add(program[idx % len(program)])
	return ''.join(moves)

def remove_programs(programs, idx, tie_move):
	remaining_programs = []
	for program in programs:
		if program[idx % len(program)] != tie_move:
			remaining_programs.append(program)
	return remaining_programs

def solve(a, programs):
	win = {'R': 'P', 'P': 'S', 'S': 'R'}
	lose = {'P': 'R', 'S': 'P', 'R': 'S'}
	tie = {
	    'PR': 'P',
	    'RP': 'P',
	    'PS': 'S',
	    'SP': 'S',
	    'RS': 'R',
	    'SR': 'R'
	}
	res = []
	i = 0
	while i <= a:
		moves = get_moves(programs, i)

		if len(moves) == 1:
			res.append(win[moves])
			return ''.join(res)

		elif len(moves) == 2:
			tie_move = tie[moves]
			res.append(tie_move)
			programs = remove_programs(programs, i, lose[tie_move])

		elif len(moves) == 3:
			return 'IMPOSSIBLE'

		i += 1

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T + 1):
		a = int(raw_input())
		program = []
		for i in range(a):
			s = raw_input()
			program.append(s)
		print "Case #{}:".format(t), solve(a, program)


assert solve(3, ['R', 'P', 'PR']) == 'PPS'
assert solve(1, ['RS']) == 'P'
assert solve(3, ['R', 'P', 'S']) == 'IMPOSSIBLE'
assert solve(7, ['RS', 'RS', 'RS', 'RS', 'RS', 'RS', 'RS']) == 'P'
assert solve(6, ['SPRSS','SRR', 'SP', 'PPSR', 'PP', 'SSPSR']) == 'IMPOSSIBLE'


# generate random test cases
# from random import randint as r, choice as c
# a = r(1, 255)
# array = []
# for _ in range(a):
# 	s = []
# 	for i in range(r(1, 500)):
# 		s.append(c(['R', 'S', 'P']))
# 	array.append(''.join(s))
# print a
# for x in array:
# 	print x
# print '---------------'
# print solve(a, array)


