import unittest
import tempfile

import numpy as np

from hw_03.src.matrix_numpy import MatrixNumpy


class MatrixNumpyTestCase(unittest.TestCase):
    def test_init_simple(self):
        m = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        self.assertEqual((3, 2), m.shape)

    def test_add_simple(self):
        m1 = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixNumpy(
            [[10, -1],
             [2, 10],
             [0, 15]]
        )
        expected = MatrixNumpy(
            [[10, 0],
             [4, 13],
             [4, 20]]
        )
        self.assertEqual(expected, m1 + m2)

    def test_add_error(self):
        m1 = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixNumpy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 + m2

    def test_mul_simple(self):
        m1 = MatrixNumpy(
            [[12, 46, 23, 7, 2],
             [3, 5, 8, 3, 6]]
        )
        m2 = MatrixNumpy(
            [[15, 26, 2, 17, 22],
             [13, 8, 9, 3, 4]]
        )
        expected = MatrixNumpy(
            [[180, 1196, 46, 119, 44],
             [39, 40, 72, 9, 24]]
        )
        self.assertEqual(expected, m1 * m2)

    def test_mul_error(self):
        m1 = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixNumpy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 * m2

    def test_matmul_simple(self):
        m1 = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixNumpy(
            [[10, -1, 0],
             [2, 10, 15]]
        )
        expected = MatrixNumpy(
            [[2, 10, 15],
             [26, 28, 45],
             [50, 46, 75]]
        )
        self.assertEqual(expected, m1 @ m2)

    def test_matmul_error(self):
        m1 = MatrixNumpy(
            [[0, 1],
             [2, 3],
             [4, 5]]
        )
        m2 = MatrixNumpy(
            [[10, -1],
             [2, 10]]
        )
        with self.assertRaises(Exception):
            m1 + m2

    def test_str(self):
        m = MatrixNumpy(
            [[0, 1],
             [2, 3]]
        )
        self.assertEqual("[[0 1]\n [2 3]]", m.__str__())

    def test_to_file(self):
        path = tempfile.mkdtemp() + "/matrix.txt"
        m = MatrixNumpy(
            [[0, 1],
             [2, 3]]
        )
        m.to_file(path)
        with open(path, "r") as f:
            lines = f.readlines()
        self.assertEqual(["[[0 1]\n", " [2 3]]"], lines)

    def test_properties(self):
        m = MatrixNumpy(
            [[0, 1],
             [2, 3]]
        )
        self.assertEqual((2, 2), m.shape)
        self.assertTrue(np.array_equal(np.array([[0, 1], [2, 3]]), m.data))
        m.data = np.array([5, 6])
        self.assertTrue(np.array_equal(np.array([5, 6]), m.data))
        with self.assertRaises(TypeError):
            m.data = "wow"
