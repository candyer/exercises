# 1
def dummy_power(n, p):
    """ return n**p"""
    if p < 0:
        return 1.0 / dummy_power(n, -p)
    total = 1
    for i in range(p): 
        total *= n
        print "p = {}".format(i+1)
    return total
print dummy_power(2, 100) 
# print dummy_power(3,  8) #6561
# print dummy_power(2, -2) #0.25

# 2
def faster_power(n, p):
    if p < 0:  return 1.0 / faster_power(n, -p)
    if p == 0: return 1
    if p == 1: return n
    sqr = n**2
    if p % 2:
        print "p = {}".format(p)
        return n * faster_power(n, p-1)
    print "p = {}".format(p)
    return faster_power(sqr, p/2)


# print faster_power(2, 100) 
# print faster_power(3,  8) #6561
# print faster_power(2, -10) #0.25
