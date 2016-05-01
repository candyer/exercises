def longestDistance(nums):
    """
    Given an array of integers, return the longest distance between two positions, num1 < num2 and pos(num1) < pos(num2)
    """
    #solution 1  Brute force     O(n^2)
    res = 0
    for i in range(len(nums)): 
        for j in range(i):
            if nums[i] > nums[j]:
                res = max(res, i-j)
    return res

    # # or we can write it in one line
    return max([0] + [i-j for i in range(len(nums)) for j in range(i) if nums[i] > nums[j]])

    #solution 2   O(n^2)
    if nums == []: return 0
    mins = []
    small = smallest = nums[0]
    index = 0
    for i in xrange(len(nums)):
        small = min(small, nums[i])
        if small == nums[i]: 
            index = i
        if smallest > small:
            smallest = small
        mins.append((smallest,index))
    
    res = 0
    for i in xrange(len(nums)-1,-1,-1):
        for j in xrange(len(mins[:i])):
            if nums[i] > mins[j][0]:
                res = max(res,(i - mins[j][1]))
    return res


    #solution 3 
    if nums == []: return 0
    mins = []
    small = smallest = nums[0]
    index = 0
    for i in xrange(len(nums)):
        small = min(small, nums[i])
        if small == nums[i]: 
            index = i
        if smallest > small:
            smallest = small
        mins.append((smallest,index))
    
    res = 0
    for i in xrange(len(nums)-1,-1,-1):
        for j in xrange(len(mins[:i])):
            if nums[i] > mins[j][0]:
                res = max(res,(i - mins[j][1]))
    return res

 
    #solution 4  O(nlogn)
    if nums == []: return 0 

    n = len(nums)
    nums_with_pos = zip(nums,range(n))
    index = list(sorted(nums_with_pos, key=lambda x: (x[0], -x[1])))

    mins = []
    small = smallest = index[0][1]
    for i in xrange(n):
        small = min(small, index[i][1])
        if smallest > small:
            smallest = small
        mins.append(smallest)

    res = max([0] + [(index[k][1] - mins[k]) for k in range(n)])
    return res 

import unittest

class MyTest(unittest.TestCase):  
    def setUp(self):
        self.nums1 = [10,9,2,5,3,7,101,18]
        self.nums2 = [10,9,2,5,3,7,2,10]
        self.nums3 = [1,2,7,11,15]
        self.nums4 = []
        self.nums5 = [9,7,5,3,4,5,2]

    def test1(self):
        self.assertEqual(longestDistance(self.nums1),7)

    def test2(self):
        self.assertEqual(longestDistance(self.nums2),6)

    def test3(self):
        self.assertEqual(longestDistance(self.nums3),4)

    def test4(self):
        self.assertEqual(longestDistance(self.nums4),0)

    def test5(self):
        self.assertEqual(longestDistance(self.nums5),2)

if __name__ == '__main__':
    unittest.main()
    
