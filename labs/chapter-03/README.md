# Lab 03 — State Preparation and Measurement Bases

**Duration:** 45–60 min · **Tools:** Python and Qiskit · **Mode:** local or Colab

## Objectives
Prepare |0⟩, |1⟩, |+⟩ and |−⟩; inspect ideal statevectors; explain why measurement distributions depend on basis.

## Step 1 — Install
```bash
python -m pip install -r labs/chapter-03/requirements.txt
```

## Step 2 — Prepare states
Build |0⟩ with an empty one-qubit circuit, |1⟩ using X, |+⟩ using H, and |−⟩ using X followed by H (or H followed by Z, with the order justified).

## Step 3 — Calculate exact probabilities
Use Statevector probabilities. Confirm that |+⟩ and |−⟩ each give (1/2, 1/2) in the computational basis.

## Step 4 — Change the measurement basis
To measure in the X basis, apply H before a computational-basis measurement. Predict the deterministic outcomes for |+⟩ and |−⟩.

## Step 5 — Validate
```bash
python -m pytest -q
```

## Exercises
1. Show that H|+⟩ = |0⟩.
2. Show that H|−⟩ = |1⟩.
3. Explain why multiplying a state by i cannot change measurement probabilities.
4. Describe the difference between a statevector probability and a finite-shot count.
