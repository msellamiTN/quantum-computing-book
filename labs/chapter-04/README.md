# Lab 04 — Tensor Products and Bell-State Preparation

**Duration:** 60–75 min · **Tools:** Python, NumPy and Qiskit · **Mode:** local or Colab

## Objectives
Construct a product state, prepare a Bell state, inspect amplitudes and verify the expected computational-basis distribution.

## Step 1 — Install
```bash
python -m pip install -r labs/chapter-04/requirements.txt
```

## Step 2 — Tensor product by hand
Use NumPy's Kronecker product to combine |+⟩ and |0⟩. Check the four amplitudes and normalization.

## Step 3 — Prepare a Bell state
Create a two-qubit circuit: H on q0, then CX(control=q0, target=q1). Inspect the statevector.

## Step 4 — Validate
The ideal state has nonzero amplitudes only for basis states 00 and 11, each with probability 1/2. The two qubits are perfectly correlated in the computational basis.

## Step 5 — Compare separable and entangled states
Prepare |+⟩⊗|0⟩ and compare its amplitudes with the Bell state. Explain why one is separable and the other is not.

## Bit ordering note
Qiskit uses qubit 0 as the least-significant bit. For a two-qubit statevector, displayed bitstrings are conventionally written q1 q0. Do not infer wire order from a printed string without checking the convention.

## Exercises
1. Construct |1⟩⊗|+⟩.
2. Prepare the Bell state (|00⟩−|11⟩)/√2.
3. Explain why its computational-basis probabilities match those of |Φ+⟩ even though the states differ.
4. Verify normalization numerically.
