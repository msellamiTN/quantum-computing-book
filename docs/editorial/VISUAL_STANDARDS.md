# Figure, Circuit and Table Standards

## Figures
Every figure has a stable identifier (e.g. `fig-01-01`), a caption (e.g. **Figure 1.1 — Classical bit and qubit representations**), an in-text reference, alt text and a source/credit record.

Store editable sources under `figures/src/` where practical; publish SVG for vector diagrams and PNG for raster figures. Use consistent restrained colors and high contrast; never use color as the only carrier of meaning. Labels must remain legible at book-page width.

### Figure register
| Field | Meaning |
|---|---|
| ID | Stable identifier |
| Caption | Reader-facing title and explanatory sentence |
| Chapter | Primary chapter |
| File | Relative path |
| Alt text | Accessible description |
| Source | Original / adapted / external |
| Credit or license | Required for non-original assets |
| Review | Scientific and editorial review state |

## Quantum circuit diagrams
When relevant, show quantum and classical registers, wire labels/direction, gates and controls, measurements and classical destinations. Gate sequence proceeds left to right. Explain register order and bitstring conventions when outputs are discussed. Check every circuit figure against the code that constructs it.

## Conceptual illustrations
Use Bloch-sphere diagrams, state vectors, probability plots and architecture flows only when they clarify a precise concept. Distinguish a schematic from a quantitatively scaled plot.

## Tables
Number per chapter (Table 1.1, Table 1.2). Give informative headers, units, assumptions and symbol definitions. Prefer editable text to screenshots.

## Charts
Include axis titles, units, sample size/shots, uncertainty where appropriate and data provenance. Explain whether values are analytical, simulated, sampled or hardware-measured.

## Accessibility and print
Alt text conveys the instructional point. Check grayscale readability and final-size legibility. Avoid tiny labels and red/green-only distinctions.
