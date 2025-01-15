from grenmlin.grn import grn
from grenmlin import simulator

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
    [{"name": "AluAND3"}],
)

# AluAND5 gate
model.add_gene(
    10,
    [
        {"name": "A0", "type": 1, "Kd": 5, "n": 4},
        {"name": "CarryIN", "type": 1, "Kd": 5, "n": 2},
    ],
    [{"name": "AluAND3"}],
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

model.plot_network()

T, Y = simulator.simulate_sequence(
    model, [(0, 100, 0, 100, 100, 0, 0) , (0, 100, 0, 0, 100, 0, 0)]
)

#print(T)
#print('-------------------------------')
#print(Y)
