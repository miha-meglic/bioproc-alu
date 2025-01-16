import unittest
from grenmlin import simulator
from alu_carry_in import generate_alu_model


def execute_alu(
    model, a0: int, a1: int, b0: int, b1: int, carry_in: int, i0: int, i1: int
) -> tuple[int, int, int]:
    T, Y = simulator.simulate_single(
        model,
        (a0, a1, b0, b1, carry_in, i0, i1),
        plot_on=False,
    )

    c0 = 1 if Y[100][-3] > 50 else 0
    c1 = 1 if Y[100][-2] > 50 else 0
    carry = 1 if Y[100][-1] > 50 else 0

    return c0, c1, carry


class TestALUCarryIn(unittest.TestCase):
    def setUp(self):
        self.model = generate_alu_model()

    def test_add_no_carry(self):
        # 01 + 10 = 11
        c0, c1, carry = execute_alu(self.model, 100, 0, 0, 100, 0, 0, 0)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 1)
        self.assertEqual(carry, 0)

    def test_add_carry_out(self):
        # 11 + 10 = (1)01
        c0, c1, carry = execute_alu(self.model, 100, 100, 0, 100, 0, 0, 0)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 0)
        self.assertEqual(carry, 1)

    def test_add_carry_in_carry_out(self):
        # 11 + 11 (+ 1) = (1)11
        c0, c1, carry = execute_alu(self.model, 100, 100, 100, 100, 100, 0, 0)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 1)
        self.assertEqual(carry, 1)

    def test_and_01(self):
        # 10 AND 01 = 00 (instruction: 01)
        c0, c1, _ = execute_alu(self.model, 0, 100, 100, 0, 0, 100, 0)

        self.assertEqual(c0, 0)
        self.assertEqual(c1, 0)

    def test_and_02(self):
        # 11 AND 01 = 01 (instruction: 01)
        c0, c1, _ = execute_alu(self.model, 100, 100, 100, 0, 0, 100, 0)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 0)

    def test_and_03(self):
        # 11 AND 11 = 01 (instruction: 01)
        c0, c1, _ = execute_alu(self.model, 100, 100, 100, 100, 0, 100, 0)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 1)

    def test_negated_a_01(self):
        # not 11 = 00 (instruction: 10)
        c0, c1, _ = execute_alu(self.model, 100, 100, 0, 0, 0, 0, 100)

        self.assertEqual(c0, 0)
        self.assertEqual(c1, 0)

    def test_negated_a_02(self):
        # not 10 = 01 (instruction: 10)
        c0, c1, _ = execute_alu(self.model, 0, 100, 0, 100, 0, 0, 100)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 0)

    def test_negated_a_03(self):
        # not 00 = 11 (instruction: 10)
        c0, c1, _ = execute_alu(self.model, 0, 0, 100, 100, 0, 0, 100)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 1)

    def test_roll_a_01(self):
        # 11 = 11 (instruction: 11)
        c0, c1, _ = execute_alu(self.model, 100, 100, 0, 0, 100, 100, 100)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 1)

    def test_roll_a_02(self):
        # 10 = 01 (instruction: 11)
        c0, c1, _ = execute_alu(self.model, 0, 100, 0, 100, 0, 100, 100)

        self.assertEqual(c0, 1)
        self.assertEqual(c1, 0)

    def test_roll_a_03(self):
        # 01 = 10 (instruction: 11)
        c0, c1, _ = execute_alu(self.model, 100, 0, 100, 100, 0, 100, 100)

        self.assertEqual(c0, 0)
        self.assertEqual(c1, 1)

    def test_roll_a_04(self):
        # 00 = 00 (instruction: 11)
        c0, c1, _ = execute_alu(self.model, 0, 0, 100, 0, 100, 100, 100)

        self.assertEqual(c0, 0)
        self.assertEqual(c1, 0)
