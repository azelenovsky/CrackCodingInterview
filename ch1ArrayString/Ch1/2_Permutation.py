#Given two strings, check if one is a permutation of another.
import unittest
from collections import Counter

def isPermuation(s1, s2): 
    if len(s1) != len(s2):
        return False
    cntr = Counter()
    for c in s1:
        cntr[c] += 1
    for c in s2:
        if cntr[c] == 0:
            return False
        cntr[c] -= 1
    return True

class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            print(test_string)
            actual = isPermuation(*test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isPermuation(*test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()