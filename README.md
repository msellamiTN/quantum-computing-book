# Quantum Computing: From Foundations to Engineering

**A Practical Handbook of Quantum Algorithms, Qiskit and Real-World Applications**  
**Informatique quantique : des fondements à l’ingénierie**

Bilingual undergraduate handbook built around **Learn → Build → Test → Evaluate**.

> Understand the concept. Build the circuit. Run the experiment. Validate the result. Understand the limitation.  
> Comprendre le concept. Construire le circuit. Exécuter l’expérience. Valider le résultat. Comprendre les limites.

## Start here
- [Editorial charter](docs/editorial/EDITORIAL_CHARTER.md)
- [24-chapter blueprint](docs/book/BOOK_BLUEPRINT.md)
- [Visual standards](docs/editorial/VISUAL_STANDARDS.md)
- [Lab standard](docs/labs/LAB_STANDARD.md)
- [English manuscript](manuscript/en/README.md)
- [Manuscrit français](manuscript/fr/README.md)
- [Lab 01](labs/chapter-01/README.md)

## Audience
Undergraduate learners with basic Python, elementary algebra and probability. No quantum physics prerequisite.

## Repository structure
```
manuscript/{en,fr}/  Bilingual chapters
figures/              Original explanatory figures and circuit diagrams
labs/                 Complete notebooks, scripts and step-by-step instructions
scripts/              Standalone examples
tests/                Numerical and software validation
docs/                 Editorial standards, roadmap and website
references/           Bibliography and bilingual glossary
.github/workflows/    CI and Pages deployment
```

## Run the first example
```bash
python -m venv .venv
# activate the environment, then:
python -m pip install -r labs/chapter-01/requirements.txt
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/chapter_01_superposition.py
```

Qiskit 2.x is the target. Pin exact versions only after clean-environment compatibility testing at release freeze.

## Scientific integrity
Distinguish exact statevector simulation, finite-shot sampling, noisy simulation and physical QPU execution. Do not claim quantum advantage without a fair reproducible comparison against strong classical baselines. State assumptions, seeds, shots, versions and limitations.

English is the master authoring language; French is a complete synchronized edition. Equations, code, figure/table IDs and exercise IDs must align.

**Status:** editorial and technical foundation prototype. Not all 24 chapters are complete, and CI/Pages deployment must be verified after this initial commit.

The manuscript license is to be finalized before book publication. Code examples use the provisional MIT license in [LICENSE-CODE](LICENSE-CODE).