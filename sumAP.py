# given n, find the sum of all the multiples of 3 and 5 below n
# e.g.  n = 10:  3 + 5 + 6 + 9 = 23

# soluton 1 brute force O(N)
def f1(n):
	res = 0
	tmp = []
	for i in range(3, n):
		if i % 3 == 0 or i % 5 == 0:
			res += i
	return res


# solution 2  number theory O(1)
def sumAP(a1, d, n):
	'''
	a1 denotes the initial term of an arithmetic progression
	d denotes the common difference
	n denotes the length of arithmetic progression
	'''
	return n * (2 * a1 + (n - 1) * d) / 2

def f2(n):
	r3 = (n - 1) / 3
	r5 = (n - 1) / 5
	r15 = (n - 1) / 15
	return sumAP(3, 3, r3) + sumAP(5, 5, r5) - sumAP(15, 15, r15)


import cProfile
cProfile.run('f1(10000000)')
cProfile.run('f2(10000000)')

...........................................................................................................
         4 function calls in 1.428 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.428    1.428 <string>:1(<module>)
        1    1.110    1.110    1.428    1.428 sumMultiple3and5.py:5(f1)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.318    0.318    0.318    0.318 {range}

...........................................................................................................
         6 function calls in 0.000 seconds
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 sumMultiple3and5.py:15(sumAP)
        1    0.000    0.000    0.000    0.000 sumMultiple3and5.py:24(f2)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
...........................................................................................................

