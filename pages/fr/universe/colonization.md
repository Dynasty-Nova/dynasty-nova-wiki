---
wiki_id: 14
locale: "fr"
path: "universe/colonization"
url: "https://wiki.dynastynova.com/fr/universe/colonization"
title: "Coloniser"
description: "Fonder des colonies avec le Pionnier spatial."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:12.330Z"
updated: "2026-10-02T17:40:33.886Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Coloniser

> **En bref** : pour fonder une colonie, envoyez un Pionnier spatial en mission Colonisation vers une position libre. Le nombre de planètes que vous pouvez posséder dépend de votre niveau de Cosmologie Appliquée : 2 planètes au niveau 1, puis une de plus tous les deux niveaux.
{.is-info}

<img src="/images/illustrations/ships/pionnier-spatial.jpg" width="180" alt="Pionnier spatial">

## Règles

1. Il faut un **Pionnier spatial** (Dock orbital 4, Moteur Magnétique 3, Cosmologie Appliquée 1) et une **place de colonie libre**.
2. **Nombre de planètes** (planète mère comprise) = 1 + partie entière((niveau de Cosmologie Appliquée + 1) / 2).
3. La cible doit être une **position libre** d'un système. L'espace lointain, au-delà de la dernière position, ne peut pas être colonisé.
4. La mission **Colonisation** est un aller simple : l'hydrogène du retour n'est pas facturé.
5. Le Pionnier spatial est **consommé** : il devient la colonie.
6. La nouvelle colonie démarre avec une **Base Coloniale**, l'équivalent de la Base planetaire, et avec les **ressources embarquées** par le Pionnier et les vaisseaux qui l'accompagnent.
7. Sa taille et sa température dépendent de sa position (voir [Planètes](/fr/universe/planets)).
8. Une planète **abandonnée** par un autre joueur peut être recolonisée : vous récupérez les bâtiments qui y restent. Son ancien propriétaire ne peut pas la reprendre pendant 30 jours.

## Exemple chiffré

Vous avez Cosmologie Appliquée niveau 3 :
- Planètes possibles : 1 + partie entière((3 + 1) / 2) = **3**, soit votre planète mère et 2 colonies.
- Monter au niveau 4 ne change rien (3 planètes). Il faut le niveau 5 pour une 4e planète.

## Données détaillées

### Planètes selon la Cosmologie Appliquée

| Niveau | 0 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Planètes au total | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

Les niveaux pairs n'ajoutent pas de planète (le niveau 2 donne autant que le niveau 1).

### Le Pionnier spatial

| Coût | Structure | Fret | Vitesse de base | Moteur | Consommation |
|---|---|---|---|---|---|
| 10 000 métal, 20 000 cristal, 10 000 hydrogène | 30 000 | 7 500 | 2 500 | Moteur Magnétique | 1 000 |

## Pièges fréquents

- **Chargez le Pionnier** : sa soute (7 500) et celle des vaisseaux qui l'accompagnent apportent les premières ressources de la colonie.
- **Le Pionnier est lent** : vitesse de base 2 500. Une colonie lointaine demande un long trajet.
- **Une colonie de plus tous les deux niveaux** : vérifiez que vous avez une place libre avant d'envoyer le Pionnier.
- **Choisissez la position** : une position proche du soleil donne une petite planète chaude (énergie solaire), une position lointaine une grande planète froide (hydrogène). Une colonie a aussi un bonus de position : jusqu'à +40 % de cristal en positions 1 à 3, jusqu'à +35 % de métal en positions 6 à 10 (voir [Planètes](/fr/universe/planets)).
- **Une planète abandonnée n'est pas vide** : ses bâtiments restants vous reviennent si vous la recolonisez, mais elle se dégrade avec le temps.

## Pages liées

- [Planètes : taille, température, type](/fr/universe/planets)
- [Abandonner une colonie](/fr/universe/abandoning-a-planet)
- [Liste des technologies](/fr/research/technologies)
- [Les missions](/fr/fleet/missions)
- [Coordonnées](/fr/universe/coordinates)
