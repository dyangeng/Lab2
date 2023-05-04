import unittest
import lab3_bmi as bmi


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(bmi.calculate_bmi(1.8, 61), 0)  # add assertion here
        self.assertEqual(bmi.calculate_bmi(1.6, 100), 1)
        self.assertEqual(bmi.calculate_bmi(1.8, 20), -1)


if __name__ == '__main__':
    unittest.main()

