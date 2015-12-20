def rotate1(l, n):
  """create a function that return a rotated list. l is a list; n is an int
  """
	if len(l) == 0 or len(l) == 1:
		return l
	if n <= 0:
		for i in range(abs(n)):
			l.append(l[0])
			l.pop(0)
		return l
	else:
		for i in range(len(l) - n%len(l)):
			l.append(l[0])
			l.pop(0)
		return l			

print rotate1([], 3)  #[]
print rotate1([1], 2)  #[1]
print rotate1(range(8), 0)  #[0, 1, 2, 3, 4, 5, 6, 7]
print rotate1(range(8), -2)  #[2, 3, 4, 5, 6, 7, 0, 1]
print rotate1(range(8), -10)  #[2, 3, 4, 5, 6, 7, 0, 1]
print rotate1(range(8), 2)  #[6, 7, 0, 1, 2, 3, 4, 5]
print rotate1(range(8), 10)  #[6, 7, 0, 1, 2, 3, 4, 5]
print rotate1(range(8), 8)   #[1, 2, 3, 4, 5, 6, 7, 0]


#better solution. complexity is O(n)
def reverse(l):
	return l[::-1]

def rotate2(l, n):
	if not l: 
		return l
	n = -n % len(l)
	first = l[:n]
	second = l[n:]
	return reverse(reverse(first) + reverse(second))

print rotate2([], 3)  #[]
print rotate2([1], 2)  #[1]
print rotate2(range(8), 0)  #[0, 1, 2, 3, 4, 5, 6, 7]
print rotate2(range(8), -2)  #[2, 3, 4, 5, 6, 7, 0, 1]
print rotate2(range(8), -10)  #[2, 3, 4, 5, 6, 7, 0, 1]
print rotate2(range(8), 2)  #[6, 7, 0, 1, 2, 3, 4, 5]
print rotate2(range(8), 10)  #[6, 7, 0, 1, 2, 3, 4, 5]
print rotate2(range(8), 8)  #[0, 1, 2, 3, 4, 5, 6, 7]

