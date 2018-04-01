

import sys

if __name__ == '__main__':	
	t = int(raw_input())
	for _ in range(t):
		lower, upper = map(int, raw_input().split())
		lower += 1
		n = int(raw_input())

		for i in range(n):
			guessed_num = (lower + upper) >> 1
			print guessed_num
			sys.stdout.flush()

			responde = raw_input()

			if responde == 'TOO_BIG':
				upper = guessed_num - 1

			elif responde == 'TOO_SMALL':
				lower = guessed_num + 1

			elif responde == 'CORRECT':
				break
