import unittest

from hw_03.src.matrix_my import MatrixMy


class MatrixMyTestCase(unittest.TestCase):
    def test_init_simple(self):
        m = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        self.assertEqual((3, 2), m.shape)

    def test_init_error(self):
        with self.assertRaises(Exception):
            MatrixMy(
                [[0, 1, 3],
                 [2, 3],
                 [4, 5]]
            )

    def test_add_simple(self):
        m1 = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixMy(
            [[10, -1],
             [2, 10],
             [0, 15]]
        )
        expected = MatrixMy(
            [[10, 0],
             [4, 13],
             [4, 20]]
        )
        self.assertEqual(expected, m1 + m2)

    def test_add_error(self):
        m1 = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixMy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 + m2

    def test_mul_simple(self):
        m1 = MatrixMy(
            [[12, 46, 23, 7, 2],
             [3, 5, 8, 3, 6]]
        )
        m2 = MatrixMy(
            [[15, 26, 2, 17, 22],
             [13, 8, 9, 3, 4]]
        )
        expected = MatrixMy(
            [[180, 1196, 46, 119, 44],
             [39, 40, 72, 9, 24]]
        )
        self.assertEqual(expected, m1 * m2)

    def test_mul_error(self):
        m1 = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixMy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 * m2

    def test_matmul_simple(self):
        m1 = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixMy(
            [[10, -1, 0],
             [2, 10, 15]]
        )
        expected = MatrixMy(
            [[2, 10, 15],
             [26, 28, 45],
             [50, 46, 75]]
        )
        self.assertEqual(expected, m1 @ m2)

    def test_matmul_error(self):
        m1 = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixMy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 + m2

    def test_hash(self):
        m = MatrixMy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        self.assertEqual(0 + 1 + 4 + 9 + 16 + 25, m.__hash__())

    def test_matmul_cache(self):
        m = MatrixMy(
            [[1, 0],
             [0, 1]]
        )
        m1 = MatrixMy(
            [[0, 1],
             [0, 0]]
        )
        m2 = MatrixMy(
            [[1, 0],
             [0, 0]]
        )
        self.assertEqual(m1.__hash__(), m2.__hash__())
        self.assertEqual(m1, m @ m1)
        self.assertEqual(m1, m @ m2)
