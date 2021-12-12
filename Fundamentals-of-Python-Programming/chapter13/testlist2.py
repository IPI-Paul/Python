# Listing 14.29
# Uses Python's unittest module to test the same functions in Listing 13.13
# Author: Rick Halterman
# Last modified: 

import unittest

#----------------- The origianl functions from before ------------------------

def max_of_three_bad(x, y, z):
    """
    Attempts to determine and return the maximum of three numeric values
    """
    result = x
    if y > result:
        result = y
    elif z > result:
        result = z
    return result

def max_of_three_good(x, y, z):
    """
    Computes and returns the maximum of three numeric values
    """
    result = x
    if y > result:
        result = y
    elif z > result:
        result = z
    return result

def sum(lst):
    """
    Attempts to compute and return the sum xof all three elements in a list of 
    integers
    """
    total = 0
    for i in range(1, len(lst)):
        total += lst[i]
    return total

# Maximum has a bug (it has yet to be written!)
def maximum(lst):
    """
    Computes the maximum element in a list of integers
    """
    return 0

#----------- Some new code to test -------------------------------------------

class ListManager(object):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst
        
    def get(self, idx):
        return self.lst[idx]

#----------- The test class --------------------------------------------------

class TestFunctionsEtc(unittest.TestCase):
    # Some test cases to test max_of_three_bad
    def test_max_of_three_bad_1(self):
        self.assertEqual(max_of_three_bad(2, 3, 4), 4)
        
    def test_max_of_three_bad_2(self):
        self.assertEqual(max_of_three_bad(4, 3, 2), 4)
        
    def test_max_of_three_bad_3(self):
        self.assertEqual(max_of_three_bad(3, 2, 4), 4)
    
    # Some test cases to test max_of_three_good
    def test_max_of_three_good_1(self):
        self.assertEqual(max_of_three_good(2, 3, 4), 4)
        
    def test_max_of_three_good_2(self):
        self.assertEqual(max_of_three_good(4, 3, 2), 4)
        
    def test_max_of_three_good_3(self):
        self.assertEqual(max_of_three_good(3, 2, 4), 4)
    
    # Some test cases to test maximum
    def test_maximum_1(self):
        self.assertEqual(maximum([2, 3, 4, 1]), 4)
        
    def test_maximum_2(self):
        self.assertEqual(maximum([4, 3, 2, 1]), 4)
        
    def test_maximum_3(self):
        self.assertEqual(maximum([-2, -3, 0, -21]), 0)
    
    # Some test cases to test sum
    def test_sum_1(self):
        self.assertEqual(sum([0, 3, 4]), 7)
        
    def test_sum_2(self):
        self.assertEqual(sum([-3, 0, 5]), 2)
    
    # Some code that can throw an exception
    def test_listmanager_1(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(2), 3)
        
    def test_listmanager_2(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(3), 3)
        
    def test_listmanager_3(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(0), 1)
        
    def test_listmanager_4(self):
        lm = ListManager([1, 2, 3])
        self.assertEqual(lm.get(0), 0)

if __name__ == '__main__':
    unittest.main()