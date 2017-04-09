# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

##################################
# for small input (1 ≤ N ≤ 10^6) #
#################################

#solution 1 .......................................................................................................
def bathroomStalls(n, k):
	d = {n:1}
	i = l = r = 0
	maxi = n
	while i < k:
		mid = maxi / 2
		l = mid
		r = maxi - mid - 1
		if not l in d:
			d[l] = 1
		else:
			d[l] += 1
		if not r in d:
			d[r] = 1
		else:
			d[r] += 1
		if d[maxi] >= 2:
			d[maxi] -= 1
		else:
			d.pop(maxi)
			maxi = max(d.keys(), key=int)
		i += 1
	return ' '.join([str(l), str(r)])
  
  
#solution 2 .......................................................................................................
  def bathroomStalls(n, k):
	d = {n : 1}
	count = [n]
	i = 0 
	length = 1

	while i <= n:
		tmp = count[i]
		l = tmp / 2
		r = tmp - l - 1
		if r < 0: break

		if not l in d:
			d[l] = d[tmp]
		else:
			d[l] += d[tmp]
		if not r in d:
			d[r] = d[tmp]
		else:
			d[r] += d[tmp]

		count.extend([l] * d[tmp])
		count.extend([r] * d[tmp])
		length += d[tmp] * 2
		if length >= k: break
		i += d[tmp]

	l = count[k - 1] / 2
	r = count[k - 1] - l - 1
	return ' '.join([str(l), str(r)])

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n, k = map(int,raw_input().split())
		print "Case #{}:".format(i), bathroomStalls(n, k)

# print bathroomStalls(40,25) =='0 0'
# print bathroomStalls(50, 33) =='0 0'
# print bathroomStalls(4,2) == '1 0'
# print bathroomStalls(5,2) == '1 0'
# print bathroomStalls(6,2) == '1 1'
# print bathroomStalls(1000, 1000) == '0 0'
# print bathroomStalls(1000,1) == '500 499'
# print bathroomStalls(312359, 156368) == '1 0'
