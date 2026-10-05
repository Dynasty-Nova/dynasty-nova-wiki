---
wiki_id: 38
locale: "fr"
path: "fleet/jump-gate"
url: "https://wiki.dynastynova.com/fr/fleet/jump-gate"
title: "Porte de saut"
description: "Déplacer une flotte instantanément entre deux lunes."
tags: ["fleet", "lune"]
published: true
created: "2026-10-02T13:08:58.343Z"
updated: "2026-10-02T17:40:21.744Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Porte de saut

> **En bref** : la Porte de saut se construit sur une lune. Elle envoie instantanément une flotte vers une autre de vos lunes équipée d'une Porte, sans temps de vol ni carburant. Elle ne transporte aucune ressource, et les deux portes doivent ensuite se recharger.
{.is-info}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Porte de saut">

## Règles

1. La Porte de saut se construit **uniquement sur une lune**.
2. Prérequis : **Base lunaire 1** et **Pliage Spatial 7**.
3. Un saut relie **deux lunes différentes du même joueur**, chacune équipée d'une Porte de saut rechargée.
4. Le saut est **instantané** et ne consomme **aucun hydrogène**.
5. **Coques seulement** : aucune ressource ne passe. Videz les soutes avant le saut.
6. Après un saut, **les deux portes** (départ et arrivée) se rechargent. La durée de recharge dépend du niveau de la Porte.
7. Un saut refusé (porte en recharge, lune non équipée) ne consomme aucune recharge.

## Exemple chiffré

Vous avez une Porte de saut niveau 3 sur la lune A et niveau 1 sur la lune B. Vous faites sauter votre flotte de A vers B.
- La flotte arrive immédiatement sur B, sans dépenser d'hydrogène.
- La porte de A se recharge en **47 minutes** (niveau 3), celle de B en **60 minutes** (niveau 1).
- Un nouveau saut depuis B ne sera possible qu'au bout de 60 minutes.

## Données détaillées

### Recharge selon le niveau

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 et plus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recharge (minutes) | 60 | 53 | 47 | 41 | 36 | 31 | 27 | 23 | 19 | 17 | 14 | 13 | 11 | 10 |

### Coût

Le coût double à chaque niveau.

| Niveau | Métal | Cristal | Hydrogène |
|---|---|---|---|
| 1 | 2 000 000 | 4 000 000 | 2 000 000 |
| 2 | 4 000 000 | 8 000 000 | 4 000 000 |
| 3 | 8 000 000 | 16 000 000 | 8 000 000 |
| 4 | 16 000 000 | 32 000 000 | 16 000 000 |
| 5 | 32 000 000 | 64 000 000 | 32 000 000 |

## Pièges fréquents

- **La recharge frappe les deux bouts** : améliorer seulement la porte de départ ne suffit pas à enchaîner les sauts, la porte d'arrivée se recharge à son propre rythme.
- **Pas de ressources** : une flotte chargée doit d'abord décharger sa cargaison.
- **Il faut deux lunes** : une seule Porte ne sert à rien.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Déplacements](/fr/fleet/movement)
- [Liste des technologies](/fr/research/technologies)
