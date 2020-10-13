#if an element is zero, entire row and column is zero.

import unittest

def zero_matrix(m):
    n_rows = len(m)
    n_cols = len(m[0])

    cols_ref = []
    rows_ref = []
    
    for r in range(n_rows):
        for c in range(n_cols):
            if m[r][c] == 0:
                rows_ref.append(r)
                cols_ref.append(c)
    
    for r in rows_ref:
        nullify_row(m,r)

    for c in cols_ref:
        nullify_col(m,r)

    return m

def nullify_row(m,r):
    for i in range(len(m[0])):
        m[r][i] = 0

def nullify_col(m,c):
    for i in range(len(m)):
        m[i][c] = 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
