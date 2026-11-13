# Lab 03 — Préparation des états et bases de mesure

**Durée :** 45–60 min · **Outils :** Python et Qiskit · **Exécution :** local ou Colab

## Objectifs
Préparer |0⟩, |1⟩, |+⟩ et |−⟩ ; inspecter les vecteurs d'état idéaux ; expliquer pourquoi la distribution de mesure dépend de la base.

## Étape 1 — Installation
```bash
python -m pip install -r labs/chapter-03/requirements.txt
```

## Étape 2 — Préparation des états
Construisez |0⟩ avec un circuit vide, |1⟩ avec X, |+⟩ avec H et |−⟩ avec X puis H (ou H puis Z, en justifiant l'ordre).

## Étape 3 — Probabilités exactes
Utilisez les probabilités du Statevector. Vérifiez que |+⟩ et |−⟩ donnent chacun (1/2, 1/2) dans la base computationnelle.

## Étape 4 — Changer de base de mesure
Pour mesurer dans la base X, appliquez H avant une mesure computationnelle. Prédisez les résultats déterministes pour |+⟩ et |−⟩.

## Étape 5 — Validation
```bash
python -m pytest -q
```

## Exercices
1. Montrez que H|+⟩ = |0⟩.
2. Montrez que H|−⟩ = |1⟩.
3. Expliquez pourquoi une phase globale i ne change pas les probabilités.
4. Distinguez probabilité exacte et fréquence mesurée sur un nombre fini d'essais.
