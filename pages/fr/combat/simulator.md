---
wiki_id: 49
locale: "fr"
path: "combat/simulator"
url: "https://wiki.dynastynova.com/fr/combat/simulator"
title: "Simulateur de combat"
description: "Préparer une attaque avec le simulateur."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:19.413Z"
updated: "2026-10-02T16:36:52.542Z"
---

# Simulateur de combat

> **En bref** : le simulateur estime l'issue d'un combat avant de l'engager. Vous pouvez y importer un rapport d'espionnage ou saisir les forces à la main. Il calcule une chance de victoire et une estimation du champ de ruines.
{.is-info}

## Règles

1. Le simulateur peut **importer un rapport d'espionnage** : les valeurs relevées sont reprises automatiquement.
2. Une catégorie que le rapport n'a **pas vue** (par exemple la flotte) est supposée **vide** : la chance de victoire affichée est alors un **minimum optimiste**. Saisissez une estimation si vous en avez une.
3. Si le rapport n'a pas atteint les **recherches** de la cible, ses technologies sont supposées **égales aux vôtres**.
4. Modifier une valeur importée fait passer la simulation en **saisie manuelle** : le rapport n'est plus utilisé.
5. Le simulateur estime aussi le **champ de ruines** d'un combat moyen, au taux de débris de votre univers.
6. Les simulations trop grandes sont refusées : le serveur limite le nombre d'unités par camp et le nombre de calculs.

## Exemple chiffré

Vous importez un rapport de niveau effectif 3 : ressources et flotte connues, mais ni défenses ni recherches. Le simulateur suppose zéro défense et des technologies égales aux vôtres. Si la cible a en réalité 20 Batteries ioniques, votre vraie chance de victoire sera **plus faible** que celle affichée.

## Pièges fréquents

- **Un rapport incomplet rend le simulateur optimiste** : complétez les catégories manquantes avant de vous fier au résultat.
- **Les technologies comptent** : si vous connaissez celles de la cible, saisissez-les.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Champs de ruines](/fr/combat/debris)
