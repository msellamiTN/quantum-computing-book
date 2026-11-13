# Lab 02 — Nombres complexes, vecteurs et portes

**Durée :** 45–60 min · **Outils :** Python, NumPy, Qiskit · **Exécution :** local ou Colab

## Objectifs
Calculer des modules complexes, normaliser des vecteurs d'état, vérifier l'unitarité et comparer un calcul matriciel au vecteur d'état exact de Qiskit.

## Étape 1 — Installation
```bash
python -m pip install -r labs/chapter-02/requirements.txt
```

## Étape 2 — Amplitudes complexes
Pour z = 3 + 4i, calculez le conjugué et |z|². Vérifiez que le résultat vaut 25, et non z².

## Étape 3 — Normalisation
Pour v = (1, i), calculez la norme et construisez le vecteur normalisé.

## Étape 4 — Vérification d'une porte
Construisez les matrices de Pauli-X et de Hadamard. Vérifiez numériquement U†U = I.

## Étape 5 — Comparaison avec Qiskit
Préparez |0⟩, appliquez X et comparez le vecteur d'état Qiskit au produit matriciel direct.

## Validation
Exécutez `python -m pytest -q`. Les tests utilisent des tolérances numériques.

## Exercices
1. Normalisez (1, 1+i).
2. Vérifiez H†H = I.
3. Appliquez X deux fois et expliquez le résultat.
4. Comparez l'effet d'une phase globale i sur les probabilités.
