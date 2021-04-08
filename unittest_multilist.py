import unittest
import multilist as multi


class TestMultiplicationOperation(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(multi.multiply_list([]), 0)

    def test_zero(self):
        self.assertEqual(multi.multiply_list([0, 1, 2, 55, 100]), 0)

    def test_one(self):
        self.assertEqual(multi.multiply_list([55]), 55)

    def test_multiple(self):
        self.assertEqual(multi.multiply_list([3, 4, 10]), 120)

    def test_multiple2(self):
        self.assertEqual(multi.multiply_list([1, 2, 3, 5, 10]), 300)

    def test_letter(self):
        self.assertEqual(multi.multiply_list(["a", 1, 2, 55, 100]), 11000)

    def test_onlyLetters(self):
        self.assertEqual(multi.multiply_list(["ab", "ac"]), 1)


if __name__ == '__main__':
    unittest.main()
