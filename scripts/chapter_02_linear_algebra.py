"""Chapter 2 numerical examples: complex amplitudes, normalization, unitarity."""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def main() -> None:
    z = 3 + 4j
    print("z =", z, "|z|^2 =", abs(z) ** 2)

    vector = np.array([1 + 0j, 1j], dtype=complex)
    normalized = vector / np.linalg.norm(vector)
    print("normalized vector:", normalized)
    print("norm:", np.linalg.norm(normalized))

    x_gate = np.array([[0, 1], [1, 0]], dtype=complex)
    h_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    identity = np.eye(2)
    assert np.allclose(x_gate.conj().T @ x_gate, identity)
    assert np.allclose(h_gate.conj().T @ h_gate, identity)

    circuit = QuantumCircuit(1)
    circuit.x(0)
    qiskit_state = Statevector.from_instruction(circuit).data
    direct_state = x_gate @ np.array([1, 0], dtype=complex)
    assert np.allclose(qiskit_state, direct_state)
    print("Qiskit state after X:", qiskit_state)


if __name__ == "__main__":
    main()
