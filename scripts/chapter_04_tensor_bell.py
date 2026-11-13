"""Chapter 4: tensor products and Bell-state preparation."""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def main() -> None:
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    zero = np.array([1, 0], dtype=complex)
    product = np.kron(plus, zero)
    print("Product state amplitudes:", product)
    assert np.isclose(np.vdot(product, product), 1.0)

    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    bell = Statevector.from_instruction(circuit)
    print(circuit.draw())
    print("Bell statevector:", bell.data)
    print("Probabilities:", bell.probabilities_dict())
    assert np.allclose(bell.probabilities(), [0.5, 0.0, 0.0, 0.5])


if __name__ == "__main__":
    main()
