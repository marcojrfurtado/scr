import unittest
from q1 import tree
from q2 import x


class TestTreePattern(unittest.TestCase):

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            tree(-1)

    def test_non_int_input(self):
        with self.assertRaises(ValueError):
            tree('k')

    def test_pattern_match(self):
        pattern= '  *\n' + \
                 ' ***\n' + \
                 '*****\n'
        self.assertEqual(pattern,tree(3))


class TestXPattern(unittest.TestCase):

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            x(-1)

    def test_non_int_input(self):
        with self.assertRaises(ValueError):
            x('k')

    def test_even_input(self):
        with self.assertRaises(ValueError):
            x(42)

    def test_pattern_match(self):
        pattern= '* *\n' + \
                 ' * \n' + \
                 '* *\n'
        self.assertEqual(pattern,x(3))

if __name__ == '__main__':
    unittest.main()