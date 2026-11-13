# Lab 04 — Produits tensoriels et préparation d'un état de Bell

**Durée :** 60–75 min · **Outils :** Python, NumPy et Qiskit · **Exécution :** local ou Colab

## Objectifs
Construire un état produit, préparer un état de Bell, inspecter ses amplitudes et vérifier la distribution attendue dans la base computationnelle.

## Étape 1 — Installation
```bash
python -m pip install -r labs/chapter-04/requirements.txt
```

## Étape 2 — Produit tensoriel à la main
Utilisez le produit de Kronecker de NumPy pour combiner |+⟩ et |0⟩. Vérifiez les quatre amplitudes et la normalisation.

## Étape 3 — Préparation d'un état de Bell
Créez un circuit à deux qubits : H sur q0, puis CX avec q0 comme contrôle et q1 comme cible. Inspectez le vecteur d'état.

## Étape 4 — Validation
L'état idéal a des amplitudes non nulles uniquement pour 00 et 11, avec une probabilité de 1/2 chacune. Les deux résultats sont parfaitement corrélés dans la base computationnelle.

## Étape 5 — Comparer état séparable et état intriqué
Préparez |+⟩⊗|0⟩ et comparez ses amplitudes à celles de l'état de Bell. Expliquez pourquoi le premier est séparable et le second ne l'est pas.

## Ordre des bits
Dans Qiskit, le qubit 0 est le bit de poids faible. Pour un vecteur d'état à deux qubits, les chaînes binaires affichées suivent conventionnellement l'ordre q1 q0. Vérifiez l'ordre avant d'interpréter les chaînes.

## Exercices
1. Construisez |1⟩ tensor |+⟩.
2. Préparez (|00⟩ − |11⟩)/√2.
3. Expliquez pourquoi |Φ+⟩ n'est pas un état produit.
4. Expliquez pourquoi la taille exponentielle du vecteur d'état ne prouve pas à elle seule un avantage quantique.
