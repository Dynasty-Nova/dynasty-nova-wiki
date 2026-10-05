---
wiki_id: 54
locale: "fr"
path: "espionage/sensor-phalanx"
url: "https://wiki.dynastynova.com/fr/espionage/sensor-phalanx"
title: "Phalange de capteur"
description: "Observer les flottes depuis une lune."
tags: ["espionage", "lune"]
published: true
created: "2026-10-02T13:09:29.181Z"
updated: "2026-10-02T17:40:24.782Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Phalange de capteur

> **En bref** : la Phalange de capteur se construit sur une lune. Elle scanne une planète de la même galaxie et révèle toutes les flottes qui en partent ou s'y dirigent : composition, mission et heure d'arrivée. Chaque scan coûte 5 000 hydrogène.
{.is-info}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Phalange de capteur">

## Règles

1. La Phalange se construit **uniquement sur une lune**.
2. Elle ne peut scanner qu'une **planète** située dans la **même galaxie**, à portée. Elle ne peut **jamais cibler une lune**.
3. **Portée** = niveau² − 1 systèmes de part et d'autre de la lune (minimum 1).
4. Chaque scan coûte **5 000 hydrogène**, pris sur la lune, même si aucune flotte n'est trouvée.
5. Le scan montre toutes les flottes qui ont la planète pour **origine ou destination**, à l'aller et au retour : **composition, mission et heure d'arrivée**. Les flottes ennemies sont incluses.
6. La **cargaison** des flottes reste invisible.
7. Le joueur scanné **n'est jamais prévenu**.
8. Un scan refusé (hors portée, autre galaxie, cible non valide) ne coûte rien.

## Exemple chiffré

Votre lune est en [3:50:8] avec une Phalange niveau 4.
- Portée : 4² − 1 = **15 systèmes** de part et d'autre, soit les systèmes 35 à 65 de la galaxie 3.
- Vous pouvez scanner une planète en [3:60:5] pour 5 000 hydrogène.
- Une planète en [3:70:5] est hors de portée. Une planète en [4:50:5] est dans une autre galaxie : impossible.
- Près du bord, la portée est tronquée : depuis [3:5:8], la même Phalange couvre les systèmes 1 à 20, car la carte n'est pas circulaire.

## Données détaillées

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Portée (systèmes de chaque côté) | 1 | 3 | 8 | 15 | 24 | 35 | 48 | 63 | 80 |

## Pièges fréquents

- **Une flotte stationnée sur une lune est invisible** : les lunes ne peuvent pas être scannées. C'est la meilleure cachette pour une flotte.
- **Le scan est payé même vide** : 5 000 hydrogène à chaque fois.
- **Prévoir l'hydrogène sur la lune** : le coût est prélevé sur la lune, pas sur la planète.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Porte de saut](/fr/fleet/jump-gate)
- [Espionner](/fr/espionage/spying)
- [Coordonnées](/fr/universe/coordinates)
