from grenmlin.grn import grn
from grenmlin import simulator


def create_alu_model():
    # Define the GRN
    # Define the GRN
    model = grn()

    model.add_input_species("A0")
    model.add_input_species("A1")
    model.add_input_species("B0")
    model.add_input_species("B1")
    model.add_input_species("CarryIN")
    model.add_input_species("I0")
    model.add_input_species("I1")

    # Internal
    model.add_species("AluAND1", 0.1)
    model.add_species("AluAND2", 0.1)
    model.add_species("AluAND3", 0.1)
    model.add_species("AluAND4", 0.1)
    model.add_species("AluAND5", 0.1)
    model.add_species("AluOR2", 0.1)
    model.add_species("AluXOR1", 0.1)
    model.add_species("AluXOR2", 0.1)
    model.add_species("AluXOR3", 0.1)
    model.add_species("AluXOR4", 0.1)
    model.add_species("MultiAAND1", 0.1)
    model.add_species("MultiAAND2", 0.1)
    model.add_species("MultiAAND3", 0.1)
    model.add_species("MultiAAND4", 0.1)
    model.add_species("MultiBAND1", 0.1)
    model.add_species("MultiBAND2", 0.1)
    model.add_species("MultiBAND3", 0.1)
    model.add_species("MultiBAND4", 0.1)

    # Outputs
    model.add_species("C0", 0.1)
    model.add_species("C1", 0.1)
    model.add_species("Carry", 0.1)

    # AluAND1 gate
    model.add_gene(
        10,
        [
            {"name": "A0", "type": 1, "Kd": 5, "n": 4},
            {"name": "B0", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluAND1"}],
    )

    # AluAND2 gate
    model.add_gene(
        10,
        [
            {"name": "A1", "type": 1, "Kd": 5, "n": 4},
            {"name": "B1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluAND2"}],
    )

    # AluXOR1 gate
    model.add_gene(
        10,
        [
            {"name": "A0", "type": -1, "Kd": 5, "n": 4},
            {"name": "B0", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR1"}],
    )
    model.add_gene(
        10,
        [
            {"name": "A0", "type": 1, "Kd": 5, "n": 4},
            {"name": "B0", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR1"}],
    )

    # AluXOR2 gate
    model.add_gene(
        10,
        [
            {"name": "A1", "type": -1, "Kd": 5, "n": 4},
            {"name": "B1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR2"}],
    )
    model.add_gene(
        10,
        [
            {"name": "A1", "type": 1, "Kd": 5, "n": 4},
            {"name": "B1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR2"}],
    )

    # AluXOR3 gate
    model.add_gene(
        10,
        [
            {"name": "AluOR2", "type": -1, "Kd": 5, "n": 4},
            {"name": "AluXOR2", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR3"}],
    )
    model.add_gene(
        10,
        [
            {"name": "AluOR2", "type": 1, "Kd": 5, "n": 4},
            {"name": "AluXOR2", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR3"}],
    )

    # AluXOR4 gate
    model.add_gene(
        10,
        [
            {"name": "CarryIN", "type": -1, "Kd": 5, "n": 4},
            {"name": "AluXOR1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR4"}],
    )
    model.add_gene(
        10,
        [
            {"name": "CarryIN", "type": 1, "Kd": 5, "n": 4},
            {"name": "AluXOR1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluXOR4"}],
    )

    # AluAND3 gate
    model.add_gene(
        10,
        [
            {"name": "AluOR2", "type": 1, "Kd": 5, "n": 4},
            {"name": "AluXOR2", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluAND3"}],
    )

    # AluAND4 gate
    model.add_gene(
        10,
        [
            {"name": "B0", "type": 1, "Kd": 5, "n": 4},
            {"name": "CarryIN", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluAND4"}],
    )

    # AluAND5 gate
    model.add_gene(
        10,
        [
            {"name": "A0", "type": 1, "Kd": 5, "n": 4},
            {"name": "CarryIN", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluAND5"}],
    )

    # AluOR1 gate
    model.add_gene(
        10,
        [
            {"name": "AluAND2", "type": 1, "Kd": 5, "n": 4},
            {"name": "AluAND3", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "Carry"}],
        logic_type="or",
    )

    # AluOR2 gate
    model.add_gene(
        10,
        [
            {"name": "AluAND1", "type": 1, "Kd": 5, "n": 4},
            {"name": "AluAND4", "type": 1, "Kd": 5, "n": 2},
            {"name": "AluAND5", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "AluOR2"}],
        logic_type="or",
    )

    # Multiplexer A

    # MultiAAND1 gate
    model.add_gene(
        10,
        [
            {"name": "AluXOR4", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": -1, "Kd": 5, "n": 2},
            {"name": "I1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiAAND1"}],
    )

    # MultiAAND2 gate
    model.add_gene(
        10,
        [
            {"name": "A0", "type": -1, "Kd": 5, "n": 4},
            {"name": "I0", "type": -1, "Kd": 5, "n": 2},
            {"name": "I1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiAAND2"}],
    )

    # MultiAAND3 gate
    model.add_gene(
        10,
        [
            {"name": "AluAND1", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": 1, "Kd": 5, "n": 2},
            {"name": "I1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiAAND3"}],
    )

    # MultiAAND4 gate
    model.add_gene(
        10,
        [
            {"name": "A1", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": 1, "Kd": 5, "n": 2},
            {"name": "I1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiAAND4"}],
    )

    # C0
    model.add_gene(
        10,
        [
            {"name": "MultiAAND1", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiAAND2", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiAAND3", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiAAND4", "type": 1, "Kd": 20, "n": 4},
        ],
        [{"name": "C0"}],
        logic_type="or",
    )

    # Multiplexer B

    # MultiBAND1 gate
    model.add_gene(
        10,
        [
            {"name": "AluXOR3", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": -1, "Kd": 5, "n": 2},
            {"name": "I1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiBAND1"}],
    )

    # MultiBAND2 gate
    model.add_gene(
        10,
        [
            {"name": "A1", "type": -1, "Kd": 5, "n": 4},
            {"name": "I0", "type": -1, "Kd": 5, "n": 2},
            {"name": "I1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiBAND2"}],
    )

    # MultiBAND3 gate
    model.add_gene(
        10,
        [
            {"name": "AluAND2", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": 1, "Kd": 5, "n": 2},
            {"name": "I1", "type": -1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiBAND3"}],
    )

    # MultiBAND4 gate
    model.add_gene(
        10,
        [
            {"name": "A0", "type": 1, "Kd": 5, "n": 4},
            {"name": "I0", "type": 1, "Kd": 5, "n": 2},
            {"name": "I1", "type": 1, "Kd": 5, "n": 2},
        ],
        [{"name": "MultiBAND4"}],
    )

    # C1
    model.add_gene(
        10,
        [
            {"name": "MultiBAND1", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiBAND2", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiBAND3", "type": 1, "Kd": 20, "n": 4},
            {"name": "MultiBAND4", "type": 1, "Kd": 20, "n": 4},
        ],
        [{"name": "C1"}],
        logic_type="or",
    )

    return model


def scaling_alu(inputA, inputB, carry_in, I0, I1):
    A = [100 if x else 0 for x in inputA]
    B = [100 if x else 0 for x in inputB]
    I0 = 100 if I0 else 0
    I1 = 100 if I1 else 0

    lA = len(A)
    lB = len(B)
    totalL = max(lA, lB)
    if totalL % 2 == 1:
        totalL += 1

    A = A + [0] * (totalL - lA)
    B = B + [0] * (totalL - lB)

    model = create_alu_model()
    results = []
    carry = carry_in

    # print(f'A: {A}')
    # print(f'B: {B}')

    for i in range(0, totalL, 2):
        T, Y = simulator.simulate_single(
            model,
            (A[i], A[i + 1], B[i], B[i + 1], carry, I0, I1),
            plot_on=False,
        )

        # print(f'Rotation {i}')

        c0 = Y[100][-3] > 50
        c1 = Y[100][-2] > 50
        carry = 100 if Y[100][-1] > 50 else 0

        # print(f'c0: {c0}')
        # print(f'c1: {c1}')
        # print(f'Carry: {carry}')

        results.extend([int(c0), int(c1)])

    return results, int(carry > 50)


if __name__ == "__main__":
    inputA = [1, 0, 0, 1]
    inputB = [1, 1, 1, 1]
    carry_in = 0
    I0 = 1
    I1 = 1
    results, carry = scaling_alu(inputA, inputB, carry_in, I0, I1)
    print(f"Results: {results}")
    print(f"Carry: {carry}")
