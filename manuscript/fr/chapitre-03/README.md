# Chapitre 3 — États quantiques et notation de Dirac

> **Parcours :** Premiers pas · **Question :** Comment décrire un état quantique indépendamment d'un circuit particulier ?

## Objectifs pédagogiques
- Lire la notation ket et bra.
- Exprimer un état dans une base orthonormée choisie.
- Appliquer la règle de Born à une base de mesure générale.
- Distinguer un vecteur d'état de sa représentation en coordonnées.
- Expliquer normalisation, orthogonalité et phase globale.

## 3.1 Kets, bras et états de base

La notation de Dirac représente un état par un ket \(|\psi\rangle\), et son transposé conjugué par un bra \(\langle\psi|\). La base computationnelle d'un qubit est
\[
|0\rangle=\begin{bmatrix}1\\0\end{bmatrix},\qquad
|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}.
\]
Ces vecteurs sont orthonormés :
\[
\langle0|0\rangle=\langle1|1\rangle=1,\quad
\langle0|1\rangle=\langle1|0\rangle=0.
\]

## 3.2 Développement dans une base

Tout état pur à un qubit se développe dans la base computationnelle :
\[
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,
\quad |\alpha|^2+|\beta|^2=1.
\]
Les coefficients dépendent de la base choisie. L'état constitue la description physique abstraite ; le vecteur en est la représentation en coordonnées dans une base donnée.

## 3.3 Mesure comme projection

Pour une mesure dans la base computationnelle, les projecteurs sont
\[
P_0=|0\rangle\langle0|,\qquad P_1=|1\rangle\langle1|.
\]
Pour un état normalisé, la probabilité du résultat \(k\) vaut
\[
p(k)=\langle\psi|P_k|\psi\rangle.
\tag{3.1}
\]
Après observation de \(k\), l'état après mesure pour cette mesure projective est \(P_k|\psi\rangle/\sqrt{p(k)}\), si \(p(k)>0\).

## 3.4 La base de mesure compte

Un même état peut produire des distributions différentes selon la base de mesure. Définissons
\[
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},\quad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}.
\]
L'état \(|+\rangle\) donne certainement + dans la base X, mais donne 0 et 1 avec la même probabilité dans la base Z (computationnelle). Une porte Hadamard avant une mesure computationnelle réalise une mesure dans la base X.

**Tableau 3.1 — États à un qubit et probabilités dans la base computationnelle**

| État | Amplitudes (0, 1) | P(0) | P(1) |
|---|---|---:|---:|
| \(|0\rangle\) | (1, 0) | 1 | 0 |
| \(|1\rangle\) | (0, 1) | 0 | 1 |
| \(|+\rangle\) | \((1/\sqrt2,1/\sqrt2)\) | 1/2 | 1/2 |
| \(|-\rangle\) | \((1/\sqrt2,-1/\sqrt2)\) | 1/2 | 1/2 |

## 3.5 Phase globale et phase relative

Multiplier tout un ket par une phase \(e^{i\phi}\) ne change aucune probabilité de mesure. Modifier une seule composante change en général la phase relative et peut affecter les interférences ultérieures. Par exemple, H transforme |+⟩ en |0⟩ et |−⟩ en |1⟩ ; le signe moins est donc physiquement pertinent relativement à l'autre composante.

## 3.6 Laboratoire pratique

[Lab 03 — Préparation d'états et bases de mesure](../../../labs/chapter-03/README.md) construit |0⟩, |1⟩, |+⟩ et |−⟩, calcule leurs vecteurs d'état et compare les mesures dans les bases Z et X.

## Vérification des connaissances
1. Quelle est la différence entre un ket et son bra ?
2. Pourquoi la somme des carrés des modules des amplitudes vaut-elle un pour un état normalisé ?
3. Quelle est la probabilité du résultat 0 pour |+⟩ dans la base Z ?
4. Comment réaliser une mesure dans la base X avec une mesure computationnelle standard ?
5. Pourquoi la phase relative est-elle observable par interférence alors que la phase globale ne l'est pas ?

## Synthèse
La notation de Dirac distingue un état de ses coordonnées, les projecteurs expriment les mesures idéales et les probabilités dépendent de la base choisie. Le chapitre 4 étend cette description à plusieurs qubits au moyen des produits tensoriels.

## Références
- Nielsen et Chuang, *Quantum Computation and Quantum Information*.
