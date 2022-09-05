import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_meterscalc(self):
        self.assertEqual(meterscalc(1), 5.0292)
