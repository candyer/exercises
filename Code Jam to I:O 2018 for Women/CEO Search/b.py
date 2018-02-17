
def solve(l, array):
	keys = array.keys()
	keys.sort()
	i = 1
	left = 0
	while i < l:
		if keys[i] == 0:
			total1 = array[keys[i]]
		else:
			total1 = keys[i] * array[keys[i]]
		total2 = array[keys[i - 1]]
		if total1 >= total2:
			left = total1 - total2
			array.pop(keys[i - 1])
		else:
			left = 0
			array[keys[i - 1]] -= total1
		if left > 0:
			j = i
			while j > 0:
				j -= 1
				if keys[j] in array:
					if array[keys[j]] >= left:
						array[keys[j]] -= left
						left = 0
						break
					else:
						left -= array[keys[j]]
					array[keys[j]] = 0
		i += 1
	key = val = 0
	for k, v in array.items():
		key = max(key, k)
		val += v
	return max(key + 1, val)

if __name__ == '__main__':
	T = int(raw_input())
	for t in range(1, T+1):
		l = int(raw_input())
		array = {}
		for _ in range(l):
			n, e = map(int,raw_input().split())
			array[e] = n
			# array.extend([e] * n)
		print "Case #{}:".format(t), solve(l, array)

