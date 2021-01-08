import unittest
from binary import bin_to_dec

class TestBinaryToDecimal(unittest.TestCase):
    """
    These help to do the code more clean
    """
    def test_binary(self):
        # Test binary numbers
        self.assertAlmostEqual(bin_to_dec(111), 7)
        self.assertAlmostEqual(bin_to_dec(101), 5)
    
    def test_values(self):
        # Make sure velues errors are raised when necessary
        self.assertRaises(ValueError, bin_to_dec, 234)
    
    # def test_types(self):
    #     self.assertRaises(TypeError, bin_to_dec, False)
    #     self.assertRaises(TypeError, bin_to_dec, 'uno')
    #     self.assertRaises(TypeError, bin_to_dec, 2+5j)
