"""Numerical checks for Chapter 1's ideal one-qubit example."""

from math import isclose

from qiskit.quantum_info import Statevector

from scripts.chapter_01_superposition import build_superposition_circuit


def test_hadamard_state_is_normalized() -> None:
    state = Statevector.from_instruction(build_superposition_circuit())
    norm_squared = float((state.data.conj() @ state.data).real)
    assert isclose(norm_squared, 1.0, abs_tol=1e-12)


def test_hadamard_probabilities_are_equal() -> None:
    probabilities = Statevector.from_instruction(build_superposition_circuit()).probabilities()
    assert len(probabilities) == 2
    assert isclose(float(probabilities[0]), 0.5, abs_tol=1e-12)
    assert isclose(float(probabilities[1]), 0.5, abs_tol=1e-12)


def test_hadamard_amplitude_magnitudes() -> None:
    state = Statevector.from_instruction(build_superposition_circuit())
    assert isclose(abs(state.data[0]), 2**-0.5, abs_tol=1e-12)
    assert isclose(abs(state.data[1]), 2**-0.5, abs_tol=1e-12)
