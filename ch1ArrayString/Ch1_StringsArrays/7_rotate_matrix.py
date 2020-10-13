import unittest

def rotate_matrix(m):
    n = len(m)
    for layer in range(n//2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            #cache top
            top = m[layer][i]

            #left to top
            m[layer][i] = m[-i - 1][layer]

            # bottom -> left
            m[-i - 1][layer] = m[-layer - 1][-i - 1]

            # right -> bottom
            m[-layer - 1][-i - 1] = m[i][- layer - 1]

            # top -> right
            m[i][- layer - 1] = top
    return m


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()