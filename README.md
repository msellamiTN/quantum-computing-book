# Quantum Computing: From Foundations to Engineering

**A Practical Handbook of Quantum Algorithms, Qiskit and Real-World Applications**  
**Informatique quantique : des fondements à l’ingénierie**

Bilingual undergraduate technical book built around **Learn → Build → Test → Evaluate**.

> Understand the concept. Build the circuit. Run the experiment. Validate the result. Understand the limitation.  
> Comprendre le concept. Construire le circuit. Exécuter l’expérience. Valider le résultat. Comprendre les limites.

## Current manuscript

- [Editorial charter](docs/editorial/EDITORIAL_CHARTER.md)
- [24-chapter blueprint](docs/book/BOOK_BLUEPRINT.md)
- [Figure, circuit and table standards](docs/editorial/VISUAL_STANDARDS.md)
- [Lab authoring standard](docs/labs/LAB_STANDARD.md)
- [English Chapters 1–4](manuscript/en/README.md)
- [Chapitres français 1–4](manuscript/fr/README.md)
- [All practical labs and notebooks](labs/)

## Audience and prerequisites
Undergraduate learners with basic Python, elementary algebra and probability. No prior quantum physics is required.

## Repository map
```text
manuscript/       Bilingual chapter sources (English master, French synchronized)
figures/          Original SVG illustrations, circuit diagrams and covers
labs/             Step-by-step notebooks, scripts and expected results
scripts/          Standalone runnable examples
tests/            Numerical and notebook-structure validation
docs/             Editorial standards, roadmap and documentation website
references/       Bibliography and bilingual glossary
.github/workflows Automated checks and GitHub Pages deployment
```

## Run the foundations labs
```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -r labs/chapter-01/requirements.txt
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/chapter_01_superposition.py
python scripts/chapter_02_linear_algebra.py
python scripts/chapter_03_measurement_bases.py
python scripts/chapter_04_tensor_bell.py
```

Qiskit 2.x is the target. Exact dependency versions must be frozen after clean-environment compatibility tests at publication release.

## Scientific integrity
Distinguish exact statevector simulation, finite-shot sampling, noisy simulation and physical QPU execution. Do not claim quantum advantage without a fair reproducible comparison against strong classical baselines. State assumptions, seeds, shots, versions and limitations.

English is the master authoring language; French is a complete synchronized edition. Equations, code, figure/table IDs and exercise IDs must align.

**Status:** Foundations prototype (Chapters 1–4) published. Remaining chapters, expanded experiments and final publication validation are still in progress.

Code examples use the provisional MIT license in [LICENSE-CODE](LICENSE-CODE). Manuscript redistribution terms must be finalized before publication.
