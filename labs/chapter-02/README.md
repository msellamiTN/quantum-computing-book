# Lab 02 — Complex Numbers, Vectors and Gates

**Duration:** 45–60 min · **Tools:** Python, NumPy, Qiskit · **Mode:** local or Colab

## Objectives
Calculate complex moduli, normalize statevectors, verify unitarity and compare a matrix calculation with Qiskit's exact statevector.

## Step 1 — Install
```bash
python -m pip install -r labs/chapter-02/requirements.txt
```

## Step 2 — Complex amplitudes
For z = 3 + 4i, calculate z conjugate and |z|². Verify that the result is 25, not z².

## Step 3 — Normalize a vector
For v = (1, i), calculate its norm and construct a normalized vector.

## Step 4 — Verify a gate
Build the Pauli-X and Hadamard matrices. Verify U†U = I numerically.

## Step 5 — Compare with Qiskit
Prepare |0⟩, apply X and compare the Qiskit statevector with direct matrix multiplication.

## Validation
Run `python -m pytest -q`. Tests use numerical tolerances.

## Exercises
1. Normalize (1, 1+i).
2. Verify H†H = I.
3. Apply X twice and explain the result.
4. Compare the effect of global phase i on computational-basis probabilities.
