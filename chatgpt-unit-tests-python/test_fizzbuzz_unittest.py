import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "fizz")
        self.assertEqual(fizzbuzz(6), "fizz")
        self.assertNotEqual(fizzbuzz(15), "fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "buzz")
        self.assertEqual(fizzbuzz(10), "buzz")
        self.assertNotEqual(fizzbuzz(15), "buzz")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "fizz buzz")
        self.assertEqual(fizzbuzz(30), "fizz buzz")

    def test_number(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)


if __name__ == "__main__":
    unittest.main()
