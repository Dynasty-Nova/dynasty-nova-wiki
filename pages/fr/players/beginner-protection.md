---
wiki_id: 57
locale: "fr"
path: "players/beginner-protection"
url: "https://wiki.dynastynova.com/fr/players/beginner-protection"
title: "Protection des débutants"
description: "Qui peut attaquer qui : protection de nouveau joueur et paliers de points."
tags: ["players"]
published: true
created: "2026-10-02T13:09:35.168Z"
updated: "2026-10-06T08:04:54.420Z"
---

# Protection des débutants

> **En bref** : deux protections empêchent les joueurs trop inégaux de se battre. La **protection de nouveau joueur** vous rend inattaquable pendant vos 7 premiers jours. La **protection par points** interdit toute attaque entre deux joueurs dont l'écart de points est trop grand, dans un sens comme dans l'autre.
{.is-info}

> **Paramètre d'univers** : les paliers de points, la durée de la protection de nouveau joueur et le délai d'inactivité peuvent être différents selon l'univers.
> Par défaut : paliers **1:3 / 1:5 / 1:10**, protection de nouveau joueur **7 jours**, inactivité **14 jours** · Redline : mêmes valeurs, sauf inactivité **7 jours**
{.is-info}

## Règles

### Protection de nouveau joueur
1. Pendant **7 jours** après votre première arrivée dans un univers, personne ne peut vous attaquer. Le temps restant s'affiche en haut de l'écran, et vos planètes portent le badge « Nouveau joueur ».
2. **Lancer une attaque ou une salve de missiles y met fin, définitivement.** Un avertissement s'affiche avant de confirmer.
3. L'espionnage, le transport et les autres missions ne la retirent pas.

### Protection par points
4. On ne peut pas attaquer un joueur **beaucoup plus faible ni beaucoup plus fort** que soi. L'écart autorisé dépend du palier du **joueur le plus faible** des deux.
5. Paliers, selon les points du plus faible :
   - moins de 500 points : écart maximal de **1:3** ;
   - de 500 à moins de 5 000 points : **1:5** ;
   - de 5 000 à moins de 500 000 points : **1:10** ;
   - 500 000 points ou plus : **plus aucune protection**.
6. Une borne appartient au palier du dessus : un joueur à exactement 5 000 points est en 1:10.
7. Un joueur protégé reste **espionnable**.
8. Les **salves de missiles** sont soumises aux mêmes règles qu'une attaque.
9. Un joueur **inactif depuis 7 jours** (sur Redline) perd sa protection : il devient attaquable par tous, quel que soit l'écart de points.
10. Les deux protections se cumulent.

## Exemple chiffré

| Joueur A | Joueur B | Palier du plus faible | Écart | Attaque possible ? |
|---|---|---|---|---|
| 400 points | 1 000 points | 1:3 (A < 500) | 2,5 | oui, dans les deux sens |
| 400 points | 1 500 points | 1:3 (A < 500) | 3,75 | **non, ni A ni B** |
| 6 000 points | 50 000 points | 1:10 (A ≥ 5 000) | 8,3 | oui, dans les deux sens |
| 6 000 points | 80 000 points | 1:10 | 13,3 | **non, ni A ni B** |
| 600 000 points | 5 000 000 points | aucun (A ≥ 500 000) | | oui |

## Pièges fréquents

- **Le plus fort est protégé aussi** : un petit joueur ne peut pas attaquer un joueur bien plus gros que lui.
- **Votre première attaque vous coûte vos 7 jours** : réfléchissez avant d'attaquer pendant votre première semaine.
- **L'inactivité lève tout** : après 7 jours sans connexion sur Redline, n'importe qui peut vous attaquer. Pensez au [mode vacances](/fr/players/vacation-mode) avant une longue absence.
- **Les points comptent tout** : économie, recherche et militaire. Construire beaucoup peut vous faire changer de palier.

## Pages liées

- [Classements et points](/fr/players/rankings)
- [Limite d'attaques](/fr/players/attack-limit)
- [Mode vacances](/fr/players/vacation-mode)
- [Inactivité](/fr/players/inactivity)
- [La vue galaxie](/fr/universe/galaxy-view)
