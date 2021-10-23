import unittest

import convert

class TestBinToHex(unittest.TestCase):
    def test_1010111001001001(self):
        self.assertEqual(convert.bin_to_hex("1010111001001001"), "0xae49")

    def test_1100100010110110010110(self):
        self.assertEqual(convert.bin_to_hex("001100100010110110010110"), "0x322d96")

class TestHexToBin(unittest.TestCase):
    def test_0x25b9d2(self):
        self.assertEqual(convert.hex_to_binary("0x25b9d2"),  "001001011011100111010010")

    def test_0xa8b3d(self):
        self.assertEqual(convert.hex_to_binary("0xa8b3d"),  "10101000101100111101")
