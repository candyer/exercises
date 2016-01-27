def longest_zero(array):
    """given a list of '0's and '1's, return the length of longest sequence of '0' """
    sequence = [0]
    count = 0
    for i in array:
        if i == 1:
            count = 0
        else:
            count += 1
        sequence.append(count)
    return max(sequence)


def longest_zero_better(array):
    """given a list of '0's and '1's, return the length of longest sequence of '0' """
    biggest = 0
    current = 0
    for i in array:
        if i == 1:
            current = 0
        else:
            current += 1
        biggest = max(biggest, current)

    return biggest



import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.array1 = [1,1,1,0,1,0,0,0,1,0]
        self.array2 = []
        self.array3 = [1,1,1,1,1]
        self.array4 = [1,1,0,0,1,1,0,0]

    def test_longest(self):
        self.assertEqual(longest_zero(self.array1), 3)
        self.assertEqual(longest_zero(self.array2), 0)
        self.assertEqual(longest_zero(self.array3), 0)
        self.assertEqual(longest_zero(self.array4), 2)

    def test_longest2(self):
        self.assertEqual(longest_zero_better(self.array1), 3)
        self.assertEqual(longest_zero_better(self.array2), 0)
        self.assertEqual(longest_zero_better(self.array3), 0)
        self.assertEqual(longest_zero_better(self.array4), 2)

if __name__ == '__main__':
    unittest.main()


# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
