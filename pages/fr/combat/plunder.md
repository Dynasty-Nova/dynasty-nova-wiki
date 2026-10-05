---
wiki_id: 46
locale: "fr"
path: "combat/plunder"
url: "https://wiki.dynastynova.com/fr/combat/plunder"
title: "Pillage"
description: "Ce que l'attaquant emporte après une victoire."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:13.859Z"
updated: "2026-10-02T16:36:48.391Z"
---

# Pillage

> **En bref** : quand l'attaquant gagne un combat, il emporte **50 % de chaque ressource** stockée sur la planète, dans la limite de la soute libre de ses vaisseaux survivants. Si la soute est trop petite, chaque ressource est réduite dans la même proportion.
{.is-info}

> **Paramètre d'univers** : la part pillée peut être différente selon l'univers.
> Par défaut et sur Redline : **50 %** de chaque ressource
{.is-info}

## Règles

1. Le pillage n'a lieu **qu'en cas de victoire** de l'attaquant. Une égalité ne rapporte rien.
2. Le butin vaut **50 % de chaque ressource** (métal, cristal, hydrogène) présente sur la planète, arrondi à l'inférieur. L'énergie n'est pas pillée.
3. Le butin est limité par la **soute libre des vaisseaux survivants**, en tenant compte du Pliage Spatial (+5 % par niveau) et de ce qui est déjà à bord.
4. Si le butin dépasse la soute, **chaque ressource est réduite dans la même proportion**. Il n'y a pas d'ordre de priorité entre les ressources.
5. Le taux ne baisse pas d'une attaque à l'autre : c'est le stock de la cible qui diminue. Piller plusieurs fois le même joueur rapporte donc de moins en moins s'il ne produit pas entre-temps.
6. Les bâtiments, les vaisseaux et les défenses ne se pillent pas.

## Exemple chiffré

La cible stocke 100 000 métal, 60 000 cristal et 20 000 hydrogène.
- Butin possible : 50 000 métal, 30 000 cristal, 10 000 hydrogène, soit **90 000**.
- Avec 10 Cargos stellaires survivants (250 000 de soute) : tout est emporté.
- Avec seulement 45 000 de soute libre, soit la moitié du butin : **25 000 métal, 15 000 cristal et 5 000 hydrogène**.
- Après un premier raid complet (90 000 emportés), il reste 50 000 métal, 30 000 cristal et 10 000 hydrogène : une seconde attaque juste après, sans production entre-temps, ne peut plus emporter que **45 000**.

## Pièges fréquents

- **Venez avec de la soute** : les vaisseaux de combat transportent peu. Ajoutez des Cargos stellaires à votre flotte d'attaque.
- **Les pertes réduisent la soute** : seuls les vaisseaux survivants emportent le butin.
- **Une égalité ne rapporte rien** : il faut éliminer toute la défense pour piller.
- **Changez de cible** : chaque raid sur le même joueur rapporte moins que le précédent.

## Pages liées

- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Limite d'attaques](/fr/players/attack-limit)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Le stockage](/fr/economy/storage)
