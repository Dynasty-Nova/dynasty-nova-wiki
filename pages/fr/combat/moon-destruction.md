---
wiki_id: 50
locale: "fr"
path: "combat/moon-destruction"
url: "https://wiki.dynastynova.com/fr/combat/moon-destruction"
title: "Destruction de lune"
description: "Détruire une lune avec des Colossus stellaires."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:21.362Z"
updated: "2026-10-02T17:40:43.107Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Destruction de lune

> **En bref** : une flotte composée uniquement de Colossus stellaires peut tenter de détruire la lune d'un autre joueur. Elle doit d'abord gagner le combat. Ensuite, deux tirages indépendants décident si la lune est détruite et si les Colossus sont perdus.
{.is-info}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Colossus stellaire">

## Règles

1. La mission **Destruction de lune** demande une flotte composée **uniquement de Colossus stellaires**, et vise la lune d'un autre joueur.
2. Un **combat classique** a lieu d'abord, contre la flotte et les défenses de la lune.
3. Les tirages n'ont lieu qu'en cas de **victoire nette** de l'attaquant.
4. Avec **S** le diamètre de la lune en km et **N** le nombre de Colossus survivants :
   - chance de **détruire la lune** = min(100, (100 − √S) × √N) % ;
   - chance de **perdre les Colossus** = √S / 2 %, en un seul tirage pour toute la flotte.
5. Les deux tirages sont **indépendants** et ont lieu tous les deux, que la lune saute ou non. Envoyer plus de Colossus n'améliore que la chance de détruire la lune : le risque de perdre la flotte ne bouge pas.
6. Si la lune est détruite : tout ce qu'elle portait disparaît, et les points correspondants sont retirés à son propriétaire. Les flottes en route vers ou depuis la lune sont redirigées vers la planète.
7. **Ni pillage, ni débris.**
8. Une lune dont le propriétaire est en vacances ne peut pas être détruite.

## Exemple chiffré

Une lune de **8 944 km** et **100 Colossus** survivants :
- √8 944 ≈ 94,6.
- Chance de détruire la lune : (100 − 94,6) × √100 ≈ **54,3 %**.
- Chance de perdre les Colossus : 94,6 / 2 ≈ **47,3 %**.

## Données détaillées

Chance de détruire une lune de 8 944 km selon le nombre de Colossus survivants (le risque de perte reste à 47,3 %) :

| Colossus survivants | 1 | 4 | 25 | 100 | 400 |
|---|---|---|---|---|---|
| Chance de destruction | 5,4 % | 10,9 % | 27,1 % | 54,3 % | 100 % |

## Pièges fréquents

- **Une grosse lune est plus dure et plus dangereuse** : plus le diamètre est grand, plus la destruction est difficile et plus le risque de perdre la flotte est élevé.
- **Le nombre ne protège pas la flotte** : le risque de perte dépend seulement du diamètre.
- **Il faut gagner le combat d'abord** : sans victoire nette, aucun tirage.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
