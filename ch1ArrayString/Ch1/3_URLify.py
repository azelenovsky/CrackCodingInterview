#Replace spaces with '%20' and remove trailing spaces
import unittest

def urlify(s, length): 
    new_idx = len(s)
    for i in reversed(range(length)):
        if s[i] == ' ':
            s[new_idx - 3:new_idx] = '%20'
            new_idx -= 3
        else:
            s[new_idx - 1] = s[i]
            new_idx -= 1
        
    return s


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()