# Practical Lab Standard

A lab is a complete learner journey, not disconnected code fragments.

## Required sections
1. Lab identity: number, title, duration estimate, difficulty and chapter link.
2. Scenario: what the learner will build or investigate.
3. Learning outcomes: observable and assessable.
4. Prerequisites: concepts, Python knowledge and required accounts.
5. Environment: Python/package versions, installation and Colab steps.
6. Inputs and files: datasets, parameters and expected directory.
7. Step-by-step procedure with complete code.
8. Circuit illustration and gate/register explanation.
9. Exact execution instructions.
10. Expected output and acceptable numerical tolerances.
11. Validation: assertions/tests and failure interpretation.
12. Experiment: change a parameter and compare.
13. Troubleshooting: common errors and diagnosis.
14. Incremental exercises and challenge task.
15. Solutions in a separate source or instructor section.
16. Reflection: what the experiment proves and does not prove.

## Artifact checklist
- Complete notebook (`.ipynb`).
- Standalone scripts where useful.
- Requirements/environment file.
- Tests for computational claims.
- README with run instructions.
- Generated output or documented expected-output example.

## Reproducibility
- No reliance on notebook execution order except top-to-bottom.
- Use explicit seeds for stochastic examples and identify seeded components.
- Compare floating-point results with tolerances.
- Never hardcode a finite-shot histogram as guaranteed output.
- Separate analytical probability from finite-shot frequency.
- Distinguish ideal simulation, noisy simulation and real QPU execution.
- Include clean-environment validation in CI when practical.
