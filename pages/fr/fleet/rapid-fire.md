---
wiki_id: 33
locale: "fr"
path: "fleet/rapid-fire"
url: "https://wiki.dynastynova.com/fr/fleet/rapid-fire"
title: "Tirs rapides"
description: "Quelles unités tirent plusieurs fois sur quelles cibles."
tags: ["fleet", "combat"]
published: true
created: "2026-10-02T13:08:48.505Z"
updated: "2026-10-02T16:36:31.430Z"
---

# Tirs rapides

> **En bref** : certains vaisseaux ont un **tir rapide** contre certaines cibles. Après avoir tiré sur l'une d'elles, ils ont une chance de tirer à nouveau dans le même round. Le facteur indiqué est le nombre moyen de tirs que le vaisseau réussit à enchaîner contre ce type de cible. Les défenses n'ont jamais de tir rapide.
{.is-info}

## Règles

1. À chaque round, chaque unité tire au moins une fois sur une cible adverse tirée au hasard parmi les unités vivantes.
2. Après chaque tir, si le tireur a un tir rapide de facteur **f** contre la cible qu'il vient de viser, il tire à nouveau avec une probabilité de **1 − 1/f**, sur une **nouvelle cible tirée au hasard**.
3. Il continue tant que le tirage réussit **et** que la nouvelle cible est elle aussi visée par un tir rapide. Si la nouvelle cible n'en fait pas partie, la chaîne s'arrête après ce tir.
4. Contre une flotte composée uniquement de la cible, le tireur tire **f fois en moyenne** par round.

## Exemple chiffré

Une Corvette a un tir rapide de **6** contre l'Intercepteur.
- Après un tir sur un Intercepteur, elle retire avec une probabilité de 1 − 1/6 = **83,3 %**.
- Face à une flotte composée uniquement d'Intercepteurs, elle tire **6 fois en moyenne** par round, au lieu d'une.
- Face à une flotte mixte (moitié Intercepteurs, moitié Cuirassés), la chaîne s'arrête dès qu'elle tombe sur un Cuirassé : elle tire nettement moins.

## Données détaillées

### Qui tire rapidement sur qui

| Tireur | Cibles (facteur) |
|---|---|
| Navette de fret | Éclaireur 5, Collecteur solaire 5 |
| Cargo stellaire | Éclaireur 5, Collecteur solaire 5 |
| Pionnier spatial | Éclaireur 5, Collecteur solaire 5 |
| Récupérateur | Éclaireur 5, Collecteur solaire 5 |
| Intercepteur | Éclaireur 5, Collecteur solaire 5 |
| Assaillant | Éclaireur 5, Collecteur solaire 5, Navette de fret 3 |
| Corvette | Projecteur balistique 10, Intercepteur 6, Éclaireur 5, Collecteur solaire 5 |
| Cuirassé | Éclaireur 5, Collecteur solaire 5 |
| Frappe-orbital | Projecteur balistique 20, Canon photonique 20, Émetteur à haute énergie 10, Batterie ionique 10, Accélérateur magnétique 5, Éjecteur à plasma 5, Éclaireur 5, Collecteur solaire 5 |
| Prédateur | Cuirassé 7, Corvette 4, Assaillant 4, Navette de fret 3, Cargo stellaire 3, Éclaireur 5, Collecteur solaire 5 |
| Annihilateur | Canon photonique 10, Prédateur 2, Éclaireur 5, Collecteur solaire 5 |
| Colossus stellaire | Éclaireur 1 250, Collecteur solaire 1 250, Pionnier spatial 250, Cargo stellaire 250, Récupérateur 250, Navette de fret 250, Projecteur balistique 200, Intercepteur 200, Canon photonique 200, Assaillant 100, Émetteur à haute énergie 100, Batterie ionique 100, Accélérateur magnétique 50, Corvette 33, Cuirassé 30, Frappe-orbital 25, Prédateur 15, Annihilateur 5 |
| Éclaireur, Collecteur solaire | aucun |
| Toutes les défenses | aucun |

### Qui est visé par quoi

| Cible | Vaisseaux qui ont un tir rapide contre elle |
|---|---|
| Éclaireur, Collecteur solaire | Tous les vaisseaux sauf l'Éclaireur et le Collecteur solaire |
| Navette de fret | Assaillant 3, Prédateur 3, Colossus 250 |
| Cargo stellaire | Prédateur 3, Colossus 250 |
| Intercepteur | Corvette 6, Colossus 200 |
| Assaillant | Prédateur 4, Colossus 100 |
| Corvette | Prédateur 4, Colossus 33 |
| Cuirassé | Prédateur 7, Colossus 30 |
| Prédateur | Annihilateur 2, Colossus 15 |
| Frappe-orbital | Colossus 25 |
| Annihilateur | Colossus 5 |
| Colossus stellaire | personne |
| Projecteur balistique | Frappe-orbital 20, Corvette 10, Colossus 200 |
| Canon photonique | Frappe-orbital 20, Annihilateur 10, Colossus 200 |
| Émetteur à haute énergie, Batterie ionique | Frappe-orbital 10, Colossus 100 |
| Accélérateur magnétique | Frappe-orbital 5, Colossus 50 |
| Éjecteur à plasma | Frappe-orbital 5 |
| Barrière défensive, Dôme protecteur | personne |

## Pièges fréquents

- **Les Éclaireurs et Collecteurs relancent les tirs adverses** : presque tous les vaisseaux ont un tir rapide de 5 contre eux. Laisser beaucoup d'Éclaireurs ou de Collecteurs en orbite pendant une attaque donne à l'attaquant des tirs supplémentaires.
- **Les tirs rapides ne garantissent rien** : la cible suivante est tirée au hasard. Dans une flotte variée, les chaînes sont plus courtes que le facteur affiché.
- **Le Colossus n'est visé par aucun tir rapide** : il ne peut être abattu qu'à la force des tirs normaux.
- **Un tir rapide ne contourne pas la règle du 1 %** : un tir trop faible contre un gros bouclier rebondit, même s'il fait partie d'une chaîne.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Simulateur de combat](/fr/combat/simulator)
