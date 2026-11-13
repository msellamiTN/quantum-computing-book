"""Chapter 3: ideal probabilities for common one-qubit states and bases."""
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def state_after(*gates: str) -> Statevector:
    circuit = QuantumCircuit(1)
    for gate in gates:
        getattr(circuit, gate)(0)
    return Statevector.from_instruction(circuit)


def main() -> None:
    examples = {
        "|0>": state_after(),
        "|1>": state_after("x"),
        "|+>": state_after("h"),
        "|->": state_after("x", "h"),
    }
    for label, state in examples.items():
        print(label, state.data, state.probabilities())
    print("X-basis measurement of |+>:", state_after("h", "h").probabilities())
    print("X-basis measurement of |->:", state_after("x", "h", "h").probabilities())


if __name__ == "__main__":
    main()
