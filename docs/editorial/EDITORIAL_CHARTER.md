# Editorial Charter

## Editorial identity
**Title:** Quantum Computing: From Foundations to Engineering  
**Subtitle:** A Practical Handbook of Quantum Algorithms, Qiskit and Real-World Applications  
**French title:** Informatique quantique : des fondements à l’ingénierie  
**French subtitle:** Un manuel pratique des algorithmes quantiques, de Qiskit et des applications réelles

This is a progressively structured undergraduate handbook with the precision and visual discipline expected of a high-quality technical publication. The editorial benchmark is professional technical publishing, including clarity associated with Eyrolles titles; this project does not claim to reproduce Eyrolles' proprietary style guide.

## Reader profile
- Undergraduate learners in computer science, engineering, mathematics or related subjects.
- Basic Python programming.
- Elementary algebra, vectors and probability.
- No prior quantum mechanics prerequisite.

## Learning model
Every unit follows **Learn → Build → Test → Evaluate**:
1. Learn: intuition, definitions, formal model and worked example.
2. Build: circuit design and implementation.
3. Test: assertions, expected output and experiment.
4. Evaluate: interpretation, limitation and transfer question.

## Chapter anatomy
1. Chapter number and informative title.
2. Learning objectives and prerequisites.
3. Motivating scenario or question.
4. Conceptual explanation, definitions and notation.
5. Mathematical development with intermediate reasoning.
6. Original explanatory figures with in-text references.
7. Numbered tables for comparisons, properties or parameters.
8. Worked examples.
9. Quantum circuit diagram and gate-by-gate interpretation.
10. Complete practical lab or companion-lab reference.
11. Knowledge check and graded exercises.
12. Summary, misconceptions and further reading.
13. References and figure/data attribution.

## Writing and typography
- Prefer precise, direct, reader-oriented prose.
- Define every new symbol at first use.
- Keep notation consistent and register order explicit.
- Number equations by chapter, e.g. (3.1), when cross-reference is useful.
- Number figures and tables by chapter: Figure 3.1, Table 3.1.
- Captions state what the reader should learn, not merely name the object.
- Put units in table headers; align decimals where meaningful.
- Keep code identifiers in monospace and preserve case.
- Define acronyms on first use.
- Use callouts sparingly for warnings, checkpoints and misconceptions.

## Bilingual policy
English is the master source. French is a complete synchronized technical edition, not an informal summary. Keep identical chapter, section, exercise, figure, table and equation identifiers; equations, symbols, code, examples, warnings and learning objectives must remain aligned. Maintain the bilingual glossary in `references/GLOSSARY_EN_FR.md`.

## Code and lab policy
All scripts and notebooks must be complete and runnable from a clean documented environment. State expected output and validation method. Pin exact versions at release freeze, after compatibility testing. No secrets or personal tokens in notebooks.

## Scientific integrity
Do not conflate superposition with classical parallel computing, measurement with reading all amplitudes, or simulation with physical hardware. A speedup/advantage claim requires a precise problem and fair comparison against a strong classical baseline. State scaling, resources, noise model, hardware and uncertainty.

## Publication review gates
Editorial; mathematical; circuit/diagram-to-code; code and clean-environment; lab usability; visual accessibility and attribution; bilingual synchronization.
