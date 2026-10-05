---
wiki_id: 11
locale: "fr"
path: "universe/coordinates"
url: "https://wiki.dynastynova.com/fr/universe/coordinates"
title: "Coordonnées"
description: "Galaxie, système, position et distances."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:06.755Z"
updated: "2026-10-02T16:36:01.684Z"
---

# Coordonnées

> **En bref** : chaque planète a une adresse à trois nombres, [galaxie:système:position], par exemple [2:83:6]. Le nombre de galaxies, de systèmes par galaxie et de positions par système dépend de l'univers (9 galaxies de 99 systèmes sur Redline). La distance entre deux coordonnées fixe la durée et le coût en hydrogène d'un vol.
{.is-info}

> **Paramètre d'univers** : le nombre de galaxies, le nombre de systèmes par galaxie et le nombre de positions par système (de 9 à 20) dépendent de l'univers.
> Redline : **9 galaxies**, **99 systèmes** par galaxie, **15 positions** par système
{.is-info}

## Règles

1. Une coordonnée s'écrit **[galaxie:système:position]**.
2. Chaque galaxie compte un nombre fixe de **systèmes**, qui dépend de l'univers : **99** sur Redline, numérotés de 1 à 99.
3. Chaque système compte un nombre fixe de **positions** (15 sur Redline). Chaque position accueille au plus une planète, et éventuellement sa lune.
4. Au-delà de la dernière position s'étend l'**espace lointain**, réservé aux expéditions.
5. **La carte n'est pas circulaire** : la galaxie 9 n'est pas voisine de la galaxie 1, et le dernier système n'est pas voisin du premier.
6. La **distance** entre deux points dépend de ce qui les sépare (table ci-dessous).

## Exemple chiffré

Depuis votre planète en [2:40:8] :
- vers [2:40:3], même système : 1 000 + 5 × 5 = **1 025**.
- vers [2:45:3], même galaxie : 2 700 + 95 × 5 = **3 175**.
- vers [5:10:1], autre galaxie : 20 000 × 3 = **60 000**.
- vers votre lune en [2:40:8] : **5**.

## Données détaillées

| Trajet | Distance |
|---|---|
| Vers une autre galaxie | 20 000 × écart de galaxies |
| Dans la même galaxie, vers un autre système | 2 700 + 95 × écart de systèmes |
| Dans le même système | 1 000 + 5 × écart de positions |
| Entre une planète et sa lune | 5 |

L'espace lointain compte comme la position qui suit la dernière : sur Redline, la position 16.

## Pièges fréquents

- **Aller d'une galaxie à l'autre coûte cher** : une seule galaxie d'écart (20 000) vaut déjà plus que la traversée complète d'une galaxie de 99 systèmes comme celles de Redline (2 700 + 95 × 98 = 12 010).
- **Pas de raccourci par le bord** : de la galaxie 1 à la galaxie 9, l'écart est de 8 galaxies.
- **Planète et lune ne sont pas au même endroit** : un trajet de 5 reste un vrai vol, très court.

## Pages liées

- [La vue galaxie](/fr/universe/galaxy-view)
- [Déplacements](/fr/fleet/movement)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Expéditions](/fr/fleet/expeditions)
