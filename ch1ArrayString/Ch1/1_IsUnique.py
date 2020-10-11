import unittest

def isUniqueSet(s): 
    return len(s) == len(set(s))


def isUniqueBasic(s):
    if len(s) > 128:
        return False
    
    char_set = [False for _ in range(128)]
    for char in s:
        val = ord(char)
        if char_set[val]:
            #Char was already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUniqueBasic(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUniqueBasic(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()