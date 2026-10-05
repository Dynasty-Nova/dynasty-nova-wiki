---
wiki_id: 40
locale: "fr"
path: "defense/defenses"
url: "https://wiki.dynastynova.com/fr/defense/defenses"
title: "Liste des défenses"
description: "Les défenses : coûts, statistiques, prérequis."
tags: ["defense", "défenses"]
published: true
created: "2026-10-02T13:09:02.050Z"
updated: "2026-10-02T17:40:06.227Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des défenses

> **En bref** : les défenses protègent votre planète en permanence. Elles ne se déplacent pas, ne peuvent pas être pillées et, après un combat, chaque défense détruite a 70 % de chances d'être réparée gratuitement. Cette page présente les 8 défenses. Les missiles ont leur propre page : [Missiles](/fr/defense/missiles).
{.is-info}

> **Paramètre d'univers** : la part des défenses détruites qui part en champ de ruines peut être différente selon l'univers.
> Par défaut : **0 %** · Redline : **0 %**
{.is-info}

## Règles

1. Les défenses se construisent au **Dock orbital**. Elles sont **payées à l'unité au moment de la mise en file**.
2. Elles participent à chaque combat livré sur leur planète, contre toute flotte attaquante.
3. **Réparation gratuite** : après un combat, chaque défense détruite fait l'objet d'un tirage indépendant. Elle a **70 % de chances** d'être réparée sans frais et 30 % d'être perdue.
4. **Barrière défensive et Dôme protecteur** : un seul exemplaire de chacun par planète. Impossible d'en commander un deuxième, ou d'en mettre un en file, tant que le premier existe. En combat, ce sont des cibles ordinaires dotées d'un très gros bouclier : ils **ne protègent pas les autres unités**.
5. Les défenses détruites ne laissent **aucun champ de ruines** (sauf réglage contraire de l'univers).
6. Les défenses détruites par un **missile** ne sont jamais réparées.
7. Les défenses n'ont **aucun tir rapide**. Certains vaisseaux, en revanche, en ont contre elles (voir [Tirs rapides](/fr/fleet/rapid-fire)).
8. En combat, l'attaque, le bouclier et la structure augmentent de 10 % par niveau de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. La **coque** en combat vaut la structure divisée par 10.
9. **Points** : chaque défense rapporte 1 point par tranche de 1 000 ressources de son coût, comptés dans les points militaires.

## Exemple chiffré

**10 Projecteurs balistiques détruits lors d'une attaque**
- Chacun a 70 % de chances d'être réparé : en moyenne **7** reviennent, mais le résultat peut aller de 0 à 10.
- Probabilité qu'ils reviennent tous les 10 : 0,7^10, soit environ **2,8 %**.

**Votre Dôme protecteur est détruit**
- 70 % de chances qu'il soit réparé, **30 % de le perdre** définitivement. Vous pourrez alors en reconstruire un.

**Un tir trop faible rebondit**
- Un tir inférieur à 1 % du bouclier de la cible n'a aucun effet.
- Un Projecteur balistique (attaque 80) entame un Cuirassé (bouclier 200, seuil 2), mais pas un Colossus stellaire (bouclier 50 000, seuil 500).

## Données détaillées

### Coûts et statistiques de base (sans recherche)

| Défense | Métal | Cristal | Hydrogène | Points | Structure | Coque en combat | Bouclier | Attaque |
|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/projecteur-balistique.jpg" width="48" alt="Projecteur balistique"> Projecteur balistique | 2 000 | 0 | 0 | 2 | 2 000 | 200 | 20 | 80 |
| <img src="/images/illustrations/defense/canon-photonique.jpg" width="48" alt="Canon photonique"> Canon photonique | 1 500 | 500 | 0 | 2 | 2 000 | 200 | 25 | 100 |
| <img src="/images/illustrations/defense/emetteur-a-haute-energie.jpg" width="48" alt="Émetteur à haute énergie"> Émetteur à haute énergie | 6 000 | 2 000 | 0 | 8 | 8 000 | 800 | 100 | 250 |
| <img src="/images/illustrations/defense/batterie-ionique.jpg" width="48" alt="Batterie ionique"> Batterie ionique | 2 000 | 6 000 | 0 | 8 | 8 000 | 800 | 500 | 150 |
| <img src="/images/illustrations/defense/accelerateur-magnetique.jpg" width="48" alt="Accélérateur magnétique"> Accélérateur magnétique | 20 000 | 15 000 | 2 000 | 37 | 35 000 | 3 500 | 200 | 1 100 |
| <img src="/images/illustrations/defense/ejecteur-a-plasma.jpg" width="48" alt="Éjecteur à plasma"> Éjecteur à plasma | 50 000 | 50 000 | 30 000 | 130 | 100 000 | 10 000 | 300 | 3 000 |
| <img src="/images/illustrations/defense/barriere-defensive.jpg" width="48" alt="Barrière défensive"> Barrière défensive | 10 000 | 10 000 | 0 | 20 | 20 000 | 2 000 | 2 000 | 1 |
| <img src="/images/illustrations/defense/dome-protecteur.jpg" width="48" alt="Dôme protecteur"> Dôme protecteur | 50 000 | 50 000 | 0 | 100 | 100 000 | 10 000 | 10 000 | 1 |

Chaque défense tire une fois par round.

### Prérequis

| Défense | Dock orbital | Recherches | Exemplaires |
|---|---|---|---|
| Projecteur balistique | 1 | aucune | illimité |
| Canon photonique | 2 | Systèmes Photoniques 3 | illimité |
| Émetteur à haute énergie | 4 | Systèmes Photoniques 6, Science Énergétique 3 | illimité |
| Batterie ionique | 4 | Manipulation Ionique 4 | illimité |
| Accélérateur magnétique | 6 | Systèmes Offensifs 3, Champs de Protection 1, Science Énergétique 6 | illimité |
| Éjecteur à plasma | 8 | Maîtrise du Plasma 7 | illimité |
| Barrière défensive | 1 | Champs de Protection 2 | 1 |
| Dôme protecteur | 6 | Champs de Protection 6 | 1 |

### Vaisseaux qui ont un tir rapide contre les défenses

| Défense | Tirs rapides subis |
|---|---|
| Projecteur balistique | Frappe-orbital 20, Corvette 10, Colossus stellaire 200 |
| Canon photonique | Frappe-orbital 20, Annihilateur 10, Colossus stellaire 200 |
| Émetteur à haute énergie | Frappe-orbital 10, Colossus stellaire 100 |
| Batterie ionique | Frappe-orbital 10, Colossus stellaire 100 |
| Accélérateur magnétique | Frappe-orbital 5, Colossus stellaire 50 |
| Éjecteur à plasma | Frappe-orbital 5 |
| Barrière défensive, Dôme protecteur | aucun |

## Pièges fréquents

- **La réparation n'est pas garantie** : 70 % est une chance par unité, pas un pourcentage du lot. Avec peu de défenses, vous pouvez toutes les perdre.
- **Les boucliers planétaires ne couvrent pas la planète** : Barrière et Dôme encaissent les tirs pour eux-mêmes, ils ne réduisent pas les dégâts subis par les autres unités.
- **Le Frappe-orbital est l'ennemi des défenses** : il a un tir rapide contre presque toutes. Face à lui, misez sur les défenses qui y échappent le mieux (Éjecteur à plasma, boucliers).
- **Les défenses ne rapportent rien à l'attaquant** : elles ne laissent pas de champ de ruines par défaut. Une planète très défendue coûte cher à attaquer sans rien rendre en débris.
- **Missiles** : une défense détruite par une Ogive longue portée est perdue pour de bon.

## Pages liées

- [Missiles](/fr/defense/missiles)
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes)
- [Tirs rapides](/fr/fleet/rapid-fire)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Liste des vaisseaux](/fr/fleet/ships)
