import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_richter_to_joule(self):
        self.assertEqual(richter_to_joule(1), 1995262.3149688789)
    
    def test_joule_to_tnt(self):
        self.assertEqual(joule_to_tnt(1995262.3149688789), 0.00047687913837688307)
