import unittest
import calc

# REF)
# https://www.youtube.com/watch?v=6tNS--WetLI

class TestCalc(unittest.TestCase):

    # Before Test class
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # After Test class
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # Before Test function
    def setUp(self):
        pass

    # After Test function
    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, 10), 20)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(5, 2), 2.5)

#         self.assertRaises(ValueError, calc.divide, 10, 0)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

