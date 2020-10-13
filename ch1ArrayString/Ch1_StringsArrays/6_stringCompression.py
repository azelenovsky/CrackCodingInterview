import unittest

def compress(s):
    compressed = []
    cntr = 0

    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            compressed.append(s[i-1] + str(cntr))
            counter = 0
        counter += 1
    
    compressed.append(s[-1] + str(counter))

    return min(s, "".join(compressed), key=len)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def compress(self):
        for [test_string, expected] in self.data:
            actual = compress(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()