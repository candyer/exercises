#leetcode 231 -- Power of Two
 
#Given an integer, write a function to determine if it is a power of two.

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0:
        return False
    if n == 1:
        return True

    while n > 1:
        if n == 2:
            return True
        if n % 2 != 0:
            return False
        n /= 2



print isPowerOfTwo(0) #False
print isPowerOfTwo(16) #True
print isPowerOfTwo(2**29) #True
print isPowerOfTwo(2) #True
print isPowerOfTwo(1) #True
print isPowerOfTwo(10) #False
print isPowerOfTwo(12) #False
print isPowerOfTwo(9) #False
print isPowerOfTwo(513) #False
print isPowerOfTwo(33) #False
print isPowerOfTwo(2**20+1) #False
print isPowerOfTwo(2**35+4) #False
print isPowerOfTwo(2**41+4) #False
print isPowerOfTwo(2**101+4) #False
print isPowerOfTwo(2**60+8) #False
