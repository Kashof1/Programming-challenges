import unittest

from main.py import *

class MyFirstTest(unittest.TestCase):

    def test_factorcalculator(self):
        self.assertEqual(factorcalculator(15), 84)

    def test_friendinputfactoradder(self):
        self.assertEqual(friendinputadder(72,84), 156) #(friend_input, factor)

    def test_hundredsdigitadder(self):
        self.assertEqual(hundredsdigitcalculator(156), 57)

    def test_


if __name__ == '__main__':
    unittest.main()