---
wiki_id: 58
locale: "fr"
path: "players/attack-limit"
url: "https://wiki.dynastynova.com/fr/players/attack-limit"
title: "Limite d'attaques"
description: "6 attaques par joueur et par tranche de 24 heures."
tags: ["players"]
published: true
created: "2026-10-02T13:09:37.126Z"
updated: "2026-10-02T16:37:05.541Z"
---

# Limite d'attaques

> **En bref** : vous pouvez attaquer un même joueur au plus **6 fois par tranche de 24 heures**, toutes ses planètes confondues, salves de missiles comprises. La tranche s'ouvre à votre première attaque contre lui. La 7e attaque est refusée dès l'envoi.
{.is-info}

> **Paramètre d'univers** : le nombre d'attaques et la durée de la tranche peuvent être différents selon l'univers (0 désactive la règle).
> Par défaut et sur Redline : **6 attaques par 24 h**
{.is-info}

## Règles

1. La limite porte sur **un joueur cible**, toutes ses planètes ensemble.
2. Comptent : les **attaques de flotte** et les **salves de missiles**. Ne comptent pas : l'espionnage, le transport, le recyclage.
3. La **tranche de 24 h est fixe** : elle s'ouvre à votre première attaque contre ce joueur et se remet à zéro 24 heures plus tard.
4. La **7e attaque** de la tranche est **refusée à l'envoi**.
5. **Rappeler** une flotte avant son arrivée rend le créneau. Une salve de missiles ne peut pas être rappelée : son créneau est consommé.
6. Les **planètes abandonnées** ne sont pas concernées.
7. Les guerres et les pactes d'alliance ne changent rien à la limite.
8. La vue galaxie affiche le nombre d'attaques qu'il vous reste contre chaque joueur.

## Exemple chiffré

| Heure | Action contre le joueur X | Attaques restantes |
|---|---|---|
| Lundi 10:00 | 1re attaque : la tranche s'ouvre jusqu'à mardi 10:00 | 5 |
| Lundi 12:00 | 2e attaque | 4 |
| Lundi 14:00 | Salve de missiles | 3 |
| Lundi 15:00 | 3e attaque de flotte, rappelée avant l'arrivée | 3 (créneau rendu) |
| Lundi 18:00 à 22:00 | 3 attaques | 0 |
| Lundi 23:00 | Nouvelle attaque : **refusée** | 0 |
| Mardi 10:00 | La tranche se remet à zéro | 6 |

## Pièges fréquents

- **La tranche ne glisse pas** : elle part de votre première attaque, pas de la dernière.
- **Les missiles comptent** : une salve est une attaque à part entière, et elle ne se rappelle pas.
- **Toutes ses planètes comptent ensemble** : attaquer deux colonies différentes d'un même joueur consomme deux créneaux.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Missiles](/fr/defense/missiles)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Pillage](/fr/combat/plunder)
