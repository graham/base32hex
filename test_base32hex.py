import unittest

import base32hex

class TestBase32Hex(unittest.TestCase):
    def test_array_to_string(self):
        x = base32hex.b32encode([0x4d, 0x88, 0xe1, 0x5b, 0x60, 0xf4,
                                 0x86, 0xe4, 0x28, 0x41, 0x2d, 0xc9])
        self.assertEqual('9m4e2mr0ui3e8a215n4g===='.upper(), x)

    def test_string_encode(self):
        x = base32hex.b32encode('base32hex_encoder')
        self.assertEqual('C9GN6P9J69K6AU2VCLN66RR4CLP0===='.upper(), x)

    def test_copy_string_from_golang(self):
        x = base32hex.b32decode('9m4e2mr0ui3e8a215n4g')
        self.assertEqual(x, [0x4d, 0x88, 0xe1, 0x5b, 0x60, 0xf4,
                             0x86, 0xe4, 0x28, 0x41, 0x2d, 0xc9])

if __name__ == '__main__':
    unittest.main()

