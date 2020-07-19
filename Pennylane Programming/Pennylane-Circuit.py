import pennylane as qml
import numpy as np

# Quantum Funciton
def my_quantum_function(x, y):
    qml.RZ(x, wires=0)
    qml.CNOT(wires=[0,1])
    qml.RY(y, wires=1)
    return qml.expval(qml.PauliZ(1))

# Defines the Computational Device. The device is and instance of the Device Class.
dev = qml.device('default.qubit', wires=2, shots=1000, analytic=False)

# Creates the Quantum Node or QNode object; a Quantum Function & Device are used.
circuit = qml.QNode(my_quantum_function, dev)

# Testing out a circuit.
circuit(np.pi/4, 0.7)
