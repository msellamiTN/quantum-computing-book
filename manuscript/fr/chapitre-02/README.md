# Chapitre 2 — Les mathématiques indispensables

> **Parcours :** Premiers pas · **Niveau :** Licence · **Prérequis :** algèbre, fonctions et probabilités élémentaires  
> **Question directrice :** Quels outils mathématiques permettent de calculer et de prévoir le comportement des circuits quantiques ?

## Objectifs pédagogiques

Vous apprendrez à :
1. manipuler les nombres complexes et calculer leur module ;
2. représenter les états quantiques par des vecteurs ;
3. calculer des produits scalaires et des normes ;
4. comprendre les matrices comme transformations linéaires ;
5. reconnaître les matrices unitaires et expliquer la conservation de la normalisation ;
6. relier les amplitudes aux probabilités.

## 2.1 Nombres complexes

Un nombre complexe s'écrit
\[
z=a+ib,\qquad a,b\in\mathbb R,\quad i^2=-1.
\]
Son conjugué est \(z^*=a-ib\), et son module vaut
\[
|z|=\sqrt{zz^*}=\sqrt{a^2+b^2}.
\]
Par exemple, pour \(z=3+4i\), on a \(z^*=3-4i\) et \(|z|^2=25\). Les probabilités quantiques sont réelles et positives ou nulles ; pour une amplitude complexe \(z\), la probabilité associée est le carré du module \(|z|^2=zz^*\), et non \(z^2\).

**Tableau 2.1 — Opérations sur les nombres complexes utilisées en quantique**

| Opération | Définition | Exemple pour \(z=3+4i\) |
|---|---|---|
| Conjugué | \(z^*\) | \(3-4i\) |
| Module au carré | \(zz^*\) | 25 |
| Partie réelle | \(\Re(z)\) | 3 |
| Partie imaginaire | \(\Im(z)\) | 4 |

## 2.2 Vecteurs et produits scalaires

Un état à un qubit s'écrit
\[
|\psi\rangle=\begin{bmatrix}\alpha\\\beta\end{bmatrix}.
\]
Le bra correspondant est le transposé conjugué :
\[
\langle\psi|=\begin{bmatrix}\alpha^*&\beta^*\end{bmatrix}.
\]
Le produit scalaire vaut \(\langle\psi|\psi\rangle=|\alpha|^2+|\beta|^2\). Un état normalisé a une norme égale à un :
\[
\langle\psi|\psi\rangle=1.
\tag{2.1}
\]
Deux états sont orthogonaux lorsque leur produit scalaire est nul.

## 2.3 Les matrices comme transformations

Une matrice agit à gauche sur un vecteur colonne. Pour un qubit :
\[
|\psi'\rangle=U|\psi\rangle.
\]
Une matrice est unitaire si
\[
U^\dagger U=UU^\dagger=I,
\tag{2.2}
\]
où \(U^\dagger\) désigne le transposé conjugué. Les transformations unitaires préservent les produits scalaires et donc la normalisation :
\[
\langle\psi'|\psi'\rangle
=\langle\psi|U^\dagger U|\psi\rangle
=\langle\psi|\psi\rangle.
\]
C'est pourquoi les portes quantiques idéales d'un système fermé sont représentées par des opérateurs unitaires.

## 2.4 Exemple : porte de Pauli-X

\[
X=\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad
X|0\rangle=|1\rangle,\quad X|1\rangle=|0\rangle.
\]
Cette matrice échange les états de la base computationnelle. Elle est unitaire car \(X^\dagger X=I\).

## 2.5 Phase globale

Les états \(|\psi\rangle\) et \(e^{i\phi}|\psi\rangle\) produisent les mêmes probabilités de mesure et représentent le même état pur physique lorsque la phase est globale. En revanche, une phase relative entre les composantes peut modifier les interférences. Cette distinction sera importante dans les chapitres suivants.

## 2.6 Laboratoire pratique

Dans [Lab 02 — Nombres complexes, vecteurs et portes](../../../labs/chapter-02/README.md), implémentez des amplitudes complexes avec NumPy, vérifiez la normalisation, construisez les matrices X et H, puis comparez les calculs matriciels au vecteur d'état fourni par Qiskit.

## Erreurs fréquentes

- Élever une amplitude complexe au carré sans prendre son module.
- Confondre un vecteur ligne et son transposé conjugué.
- Considérer toute matrice comme une porte quantique valide : une porte idéale doit être unitaire.
- Confondre phase globale et phase relative.

## Vérification des connaissances

1. Calculez \(|2-3i|^2\).
2. Normalisez \((1,1)^T\).
3. Vérifiez que la matrice de Pauli-X est unitaire.
4. Expliquez pourquoi une transformation unitaire préserve la norme d'un état normalisé.
5. Une phase globale modifie-t-elle les probabilités dans la base computationnelle ?

## Synthèse

Le conjugué complexe, les normes, les produits scalaires et les matrices unitaires constituent le langage mathématique de base des états purs quantiques. Le chapitre suivant utilise ces outils pour décrire les états et les mesures de manière systématique.

## Références

- Nielsen et Chuang, *Quantum Computation and Quantum Information*.
- Documentation Qiskit : https://docs.quantum.ibm.com/
