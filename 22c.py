#coding:utf-8
import unittest


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = 5 - 4
        hope = 1
        self.assertEqual(result,hope)

    def test_div(self):
        result1 = 7/3
        hope1 = '6s'
        self.assertEqual(result1,hope1)

if __name__ == '__main__':
    unittest.main(-v)



import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()