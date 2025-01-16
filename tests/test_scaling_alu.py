import unittest
from scaling_alu import scaling_alu


class TestALUCarryIn(unittest.TestCase):
    def test_add_no_carry(self):
        # 0111 + 110 = 1101
        result, carry = scaling_alu([1, 1, 1, 0], [0, 1, 1], 0, 0, 0)

        self.assertEqual(result, [1, 0, 1, 1])
        self.assertEqual(carry, 0)

    def test_add_carry_out(self):
        # 1111 + 0110 = (1)0101
        result, carry = scaling_alu([1, 1, 1, 1], [0, 1, 1, 0], 0, 0, 0)

        self.assertEqual(result, [1, 0, 1, 0])
        self.assertEqual(carry, 1)

    # def test_add_carry_in_carry_out(self):
    #     # 1111 + 0110 (+ 1) = (1)0110
    #     result, carry = scaling_alu([1, 1, 1, 1], [0, 1, 1, 0], 1, 0, 0)

    #     self.assertEqual(result, [0, 1, 1, 0])
    #     self.assertEqual(carry, 1)
