# leetcode 217 -- Contains Duplicate

# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, 
# return false if every element is distinct.

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))

import unittest
class MyTest(unittest.TestCase):

    def setUp(self):
        self.array1 = []
        self.array2 = [8,19,3,288,47,0]
        self.array3 = [2,4,2,5,6,7,3,1]

    def test_longest(self):
        self.assertEqual(containsDuplicate(self.array1), False)
        self.assertEqual(containsDuplicate(self.array2), False)
        self.assertEqual(containsDuplicate(self.array3), True)

if __name__ == '__main__':
    unittest.main()


.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
