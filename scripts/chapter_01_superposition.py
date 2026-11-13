"""Chapter 1: build and inspect an ideal one-qubit superposition."""

from __future__ import annotations

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def build_superposition_circuit() -> QuantumCircuit:
    """Return a one-qubit circuit with a Hadamard gate."""
    circuit = QuantumCircuit(1)
    circuit.h(0)
    return circuit


def main() -> None:
    circuit = build_superposition_circuit()
    state = Statevector.from_instruction(circuit)

    print("Circuit:")
    print(circuit.draw())
    print("\nStatevector:")
    print(state)
    print("\nExact ideal probabilities:")
    for outcome, probability in state.probabilities_dict().items():
        print(f"  {outcome}: {probability:.6f}")


if __name__ == "__main__":
    main()
