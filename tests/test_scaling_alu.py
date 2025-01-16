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

    def test_add_carry_in_carry_out(self):
        # 1111 + 0110 (+ 1) = (1)0110
        result, carry = scaling_alu([1, 1, 1, 1], [0, 1, 1, 0], 1, 0, 0)

        self.assertEqual(result, [0, 1, 1, 0])
        self.assertEqual(carry, 1)

    def test_and_01(self):
        # 0110 AND 0011 = 0010
        result, _ = scaling_alu([0, 1, 1, 0], [1, 1], 0, 1, 0)

        self.assertEqual(result, [0, 1, 0, 0])

    def test_and_02(self):
        # 0011 AND 0101 = 001
        result, _ = scaling_alu([1, 1, 0, 0], [1, 0, 1, 0], 1, 1, 0)

        self.assertEqual(result, [1, 0, 0, 0])

    def test_and_03(self):
        # 11111111 AND 10101010 = 10101010
        result, _ = scaling_alu(
            [1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], 0, 1, 0
        )

        self.assertEqual(result, [0, 1, 0, 1, 0, 1, 0, 1])

    def test_negated_a_01(self):
        # not 1111 = 0000
        result, _ = scaling_alu([1, 1, 1, 1], [], 0, 0, 1)

        self.assertEqual(result, [0, 0, 0, 0])

    def test_negated_a_02(self):
        # not 1010 = 0101
        result, _ = scaling_alu([0, 1, 0, 1], [], 1, 0, 1)

        self.assertEqual(result, [1, 0, 1, 0])

    def test_roll_a(self):
        self.assertRaises(NotImplementedError, scaling_alu, [1, 1, 1, 1], [], 0, 1, 1)
