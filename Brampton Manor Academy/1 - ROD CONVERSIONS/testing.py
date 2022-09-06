import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_meterscalc(self):
        self.assertEqual(meterscalc(1), 5.0292)
    
    def test_furlongcalc(self):
        self.assertEqual(furlongcalc(10), 0.25)

    def test_milescalc(self):
        self.assertEqual(milescalc(50.292), 0.03125007767159208)
    
    def test_feetcalc(self):
        self.assertEqual(feetcalc(50.292), 165.0)

    def test_minutes_to_walkcalc(self):
        self.assertEqual(minutes_to_walkcalc(0.03125007767159208), 0.6048402129985564)