---
wiki_id: 42
locale: "fr"
path: "defense/missiles"
url: "https://wiki.dynastynova.com/fr/defense/missiles"
title: "Missiles"
description: "Arsenal balistique, Intercepteurs et Ogives longue portée."
tags: ["defense", "missiles"]
published: true
created: "2026-10-02T13:09:06.140Z"
updated: "2026-10-02T17:40:28.005Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Missiles

> **En bref** : les missiles se stockent dans l'Arsenal balistique. Les **Ogives longue portée** détruisent les défenses d'une planète ennemie sans engager de flotte. Les **Intercepteurs** servent à abattre les Ogives qui visent votre planète. Les missiles ne prennent jamais part aux combats de flottes.
{.is-info}

> **Paramètre d'univers** : la limite d'attaques, qui compte aussi les salves de missiles, peut être différente selon l'univers.
> Par défaut : **6 attaques par 24 h** · Redline : **6 attaques par 24 h**
{.is-info}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Arsenal balistique"> <img src="/images/illustrations/defense/intercepteurs.jpg" width="180" alt="Intercepteurs"> <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="180" alt="Ogives longue portée">

## Règles

### L'Arsenal balistique
1. Les missiles sont stockés dans l'**Arsenal balistique**, qui offre **10 emplacements par niveau**.
2. Un **Intercepteur** occupe **1 emplacement**, une **Ogive longue portée** en occupe **2**.
3. Les missiles en file d'attente ou en construction comptent déjà dans les emplacements.
4. Les missiles n'occupent aucune case de la planète. Seul l'Arsenal lui-même occupe une case par niveau.
5. Démolir un niveau d'Arsenal alors qu'il est plein ne détruit aucun missile.

### Les missiles
6. Les missiles **ne tirent jamais pendant un combat** et ne comptent pas dans la puissance défensive de la planète.
7. Une salve d'Ogives **ne détruit que des défenses** : jamais les bâtiments, la flotte en orbite ni les ressources.
8. Les défenses détruites par une Ogive sont **perdues définitivement** : elles ne bénéficient pas de la réparation gratuite à 70 %.
9. **Ordre des cibles** : sans cible désignée, les Ogives frappent d'abord la défense la plus robuste (bouclier + coque). Si vous désignez une cible, elle est frappée en premier, puis le reste par robustesse décroissante. Si la planète n'a pas la défense désignée, l'ordre normal s'applique.
10. Une salve **ne peut pas être rappelée**. Les Ogives ne reviennent jamais, même si la planète cible est abandonnée entre-temps.

### Restrictions
11. Une salve **compte comme une attaque** dans la limite d'attaques sur le joueur visé, toutes ses planètes confondues. Comme elle ne peut pas être rappelée, le créneau est consommé pour de bon.
12. La **protection des débutants** s'applique : un joueur protégé ne peut pas être visé.
13. Lancer une salve **met fin à votre propre protection de nouveau joueur**, définitivement.
14. Un joueur **en mode vacances** ne peut pas être visé, et vous ne pouvez pas tirer pendant vos propres vacances.
15. Pendant une **maintenance**, les frappes de missiles sont suspendues.

## Exemple chiffré

**Remplir un Arsenal balistique niveau 3**
- Capacité : 3 × 10 = **30 emplacements**.
- 10 Intercepteurs (10 emplacements) + 10 Ogives longue portée (20 emplacements) = 30 : l'Arsenal est plein.
- Coût des 10 Ogives : 125 000 métal, 25 000 cristal, 100 000 hydrogène. Une fois tirées, elles sont retirées de vos points militaires (250 points).

**Une salve sans cible désignée** contre une planète défendue par 1 Dôme protecteur, 5 Batteries ioniques et 20 Projecteurs balistiques
- Le Dôme protecteur est la défense la plus robuste : il est frappé en premier, puis les Batteries ioniques, puis les Projecteurs.
- Tout ce qui est détruit est perdu, sans réparation.

## Données détaillées

### Missiles

| Missile | Métal | Cristal | Hydrogène | Points | Emplacements | Structure | Attaque | Prérequis |
|---|---|---|---|---|---|---|---|---|
| Intercepteurs | 8 000 | 2 000 | 0 | 10 | 1 | 8 000 | 1 | Dock orbital 1, Arsenal balistique 2 |
| Ogives longue portée | 12 500 | 2 500 | 10 000 | 25 | 2 | 15 000 | 12 000 | Dock orbital 1, Arsenal balistique 4, Moteur Magnétique 1 |

Les missiles comptent dans les points militaires.

### Arsenal balistique

Prérequis : Dock orbital 1. Niveau maximum : 10. Le coût double à chaque niveau.

| Niveau | Métal | Cristal | Hydrogène | Emplacements |
|---|---|---|---|---|
| 1 | 20 000 | 20 000 | 1 000 | 10 |
| 2 | 40 000 | 40 000 | 2 000 | 20 |
| 3 | 80 000 | 80 000 | 4 000 | 30 |
| 4 | 160 000 | 160 000 | 8 000 | 40 |
| 5 | 320 000 | 320 000 | 16 000 | 50 |
| 6 | 640 000 | 640 000 | 32 000 | 60 |
| 7 | 1 280 000 | 1 280 000 | 64 000 | 70 |
| 8 | 2 560 000 | 2 560 000 | 128 000 | 80 |
| 9 | 5 120 000 | 5 120 000 | 256 000 | 90 |
| 10 | 10 240 000 | 10 240 000 | 512 000 | 100 |

## Pièges fréquents

- **« Intercepteurs » n'est pas l'« Intercepteur »** : le missile (pluriel) et le vaisseau de combat (singulier) n'ont rien à voir.
- **Le Dôme part en premier** : sans cible désignée, la défense la plus robuste est frappée d'abord. Désignez une cible si vous visez autre chose.
- **Une salve coûte un créneau d'attaque** : elle compte dans la limite d'attaques sur le joueur, même si elle ne détruit rien.
- **Fin de la protection de nouveau joueur** : votre première salve y met fin, comme une attaque de flotte.
- **Les missiles ne défendent pas contre les flottes** : seuls les Intercepteurs servent en défense, et uniquement contre les Ogives.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Limite d'attaques](/fr/players/attack-limit)
- [Protection des débutants](/fr/players/beginner-protection)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Maintenance](/fr/misc/maintenance)
