# Lab 01 — First Qubit and Superposition

**Level:** Beginner · **Duration:** 30–45 minutes · **Execution:** local Python or Google Colab  
**Companion:** Chapter 1 — What Is Quantum Computing?

## Scenario
Create a one-qubit circuit, apply a Hadamard gate, inspect its ideal statevector, then compare theoretical probabilities with finite-shot sampling in an optional simulator extension.

## Learning outcomes
- Create and draw a Qiskit circuit.
- Apply Hadamard and inspect a statevector.
- Calculate ideal probabilities.
- Explain finite-shot fluctuations.
- Distinguish statevector simulation, shot sampling and physical QPU execution.

## Step 1 — Prepare
Create a virtual environment and install declared dependencies:
```bash
python -m venv .venv
# Activate it, then:
python -m pip install -r labs/chapter-01/requirements.txt
python -m pip install -r requirements-dev.txt
```
In Colab, open `first_qubit.ipynb` and execute its installation cell.

## Step 2 — Build
Run:
```bash
python scripts/chapter_01_superposition.py
```
The circuit starts in |0⟩. The Hadamard gate transforms it into (|0⟩ + |1⟩)/√2.

## Step 3 — Inspect exact probabilities
The statevector gives ideal probabilities of 0.5 for outcome 0 and 0.5 for outcome 1. Floating-point formatting may differ.

## Step 4 — Experiment
In the notebook, add a measurement and run a shot-based simulator as an extension. The histogram is empirical; it is not guaranteed to be exactly 50/50.

## Step 5 — Validate
```bash
python -m pytest -q
```
The tests check state normalization and ideal probabilities within numerical tolerance. They do not assert a particular finite-shot histogram.

## Expected observations

| Quantity | Expected value |
|---|---:|
| State norm | 1 |
| P(0), ideal | 0.5 |
| P(1), ideal | 0.5 |
| Finite-shot counts | Vary between runs |

## Troubleshooting
- **ImportError:** activate the intended environment and reinstall requirements.
- **Wrong notebook kernel:** select the environment's Python kernel.
- **Counts not exactly 50/50:** expected for finite shots.
- **Unexpected bitstring ordering in larger circuits:** inspect register and classical-bit ordering before interpreting results.

## Exercises
1. Replace H with X. Predict the state and outcome.
2. Apply H twice. Show why the state returns to |0⟩.
3. Change the shot count and describe sampling variability.
4. Explain why an exact statevector is not a measurement record.

## Completion criteria
You can run the script, explain the circuit, justify its ideal probabilities and distinguish exact simulation from sampling.
