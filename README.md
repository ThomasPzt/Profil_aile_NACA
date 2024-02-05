# Générateur de Profil NACA

## Introduction
Ce programme génère la forme d'un profil aérodynamique NACA 4 chiffres symétrique en fonction des paramètres fournis par l'utilisateur.

## Utilisation
1. L'utilisateur doit fournir le numéro du profil NACA, la longueur de la corde, le nombre de points pour le tracé, et le type de distribution de points le long de la corde (linéaire ou non-uniforme).
2. Le programme construit les tableaux de coordonnées pour l'extrados et l'intrados.
3. Il calcule l'épaisseur maximale et la position de ce maximum le long de la corde.
4. Le résultat est affiché dans un graphique généré avec Matplotlib, montrant la forme du profil avec une légende, un quadrillage, des étiquettes sur les axes, et un titre.

## Exécution
Exécutez le programme et suivez les instructions pour fournir les paramètres nécessaires. En cas d'erreur, des messages informatifs seront affichés pour guider l'utilisateur.

## Dépendances
- Numpy
- Matplotlib

## Auteur
Thomas Poizot
