"""Numerical regression tests for the mathematical foundations labs."""
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def test_x_and_h_are_unitary():
    x = np.array([[0, 1], [1, 0]], dtype=complex)
    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    identity = np.eye(2)
    assert np.allclose(x.conj().T @ x, identity)
    assert np.allclose(h.conj().T @ h, identity)


def test_global_phase_preserves_probabilities():
    state = Statevector([1 / np.sqrt(2), 1j / np.sqrt(2)])
    phased = Statevector(1j * state.data)
    assert np.allclose(state.probabilities(), phased.probabilities())


def test_hadamard_maps_plus_and_minus_to_basis_states():
    plus = Statevector([1 / np.sqrt(2), 1 / np.sqrt(2)])
    minus = Statevector([1 / np.sqrt(2), -1 / np.sqrt(2)])
    h = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
    assert np.allclose(h @ plus.data, [1, 0])
    assert np.allclose(h @ minus.data, [0, 1])


def test_bell_state_probabilities_and_normalization():
    circuit = QuantumCircuit(2)
    circuit.h(0)
    circuit.cx(0, 1)
    state = Statevector.from_instruction(circuit)
    assert np.isclose(np.vdot(state.data, state.data), 1.0)
    assert np.allclose(state.probabilities(), [0.5, 0.0, 0.0, 0.5])


def test_product_state_is_normalized():
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    zero = np.array([1, 0], dtype=complex)
    product = np.kron(plus, zero)
    assert np.isclose(np.vdot(product, product), 1.0)
