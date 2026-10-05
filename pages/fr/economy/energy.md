---
wiki_id: 19
locale: "fr"
path: "economy/energy"
url: "https://wiki.dynastynova.com/fr/economy/energy"
title: "L'énergie"
description: "Produire et consommer de l'énergie, déficit et taux de fonctionnement."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:22.054Z"
updated: "2026-10-02T17:40:48.927Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# L'énergie

> **En bref** : vos mines consomment de l'énergie, vos centrales en produisent. Tant que la production couvre la consommation, tout tourne à plein régime. Dès qu'elle ne suffit plus, **toutes** les mines ralentissent dans la même proportion. L'énergie ne se stocke pas.
{.is-info}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Capteurs photovoltaïques"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Réacteur thermonucléaire"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Collecteur solaire">

## Règles

1. **Sources d'énergie** :
   - **Capteurs photovoltaïques** : bâtiment, produit davantage quand la température actuelle de la planète est élevée (× (1 + température actuelle / 100) quand elle est positive).
   - **Réacteur thermonucléaire** : bâtiment, produit de l'énergie en **consommant de l'hydrogène**. Sa production augmente avec la Science Énergétique.
   - **Collecteur solaire** : vaisseau qui reste en orbite. Il produit davantage sur une planète chaude, mais il peut être **détruit lors d'une attaque**.
2. **Consommation** : l'Excavateur minéral, l'Extracteur cristallin et le Condensateur d'hydrogène consomment de l'énergie, de plus en plus à chaque niveau.
3. **Déficit** : si la consommation dépasse la production, la production de métal, de cristal et d'hydrogène est réduite **dans la même proportion**. Une ligne « Déficit d'énergie » apparaît dans le détail de production.
4. **Taux de fonctionnement** : chaque mine se règle par **pas de 10 %**. Baisser le taux réduit à la fois sa production et sa consommation, dans la même proportion.
5. L'énergie **n'est jamais stockée** : elle se calcule à chaque instant.
6. Certains bâtiments et technologies demandent une **énergie requise** pour être lancés (Station de réparation, Modulateur planétaire, Manipulation Gravitationnelle) : c'est un seuil de production, pas une dépense.

## Exemple chiffré

Votre planète produit **1 000** énergie et vos mines en demandent **1 250**.
- Taux de couverture : 1 000 / 1 250 = **80 %**.
- Toutes les mines tournent à 80 % : un Excavateur qui devrait produire 2 000 métal/h n'en produit plus que **1 600**.
- Ajouter un niveau de mine aggrave le déficit : il vaut mieux ajouter une centrale.

## Données détaillées

### Consommation relevée en jeu

| Niveau | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Excavateur ou Extracteur | 448 | 531 | 626 | 735 | 859 | 1 000 | 1 162 | 1 345 | 1 554 | 1 790 |

| Niveau | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|
| Condensateur d'hydrogène | 212 | 259 | 313 | 376 | 448 | 531 | 626 | 735 | 859 | 1 000 |

### Production relevée en jeu

Capteurs photovoltaïques, un jour où la température actuelle était de 23 °C :

| Niveau | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Énergie | 1 104 | 1 307 | 1 541 | 1 808 | 2 113 | 2 461 | 2 858 | 3 309 | 3 822 | 4 405 |

Réacteur thermonucléaire, avec Science Énergétique 3 :

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Énergie produite | 32 | 69 | 113 | 163 | 220 | 285 | 359 | 444 | 539 | 647 |
| Hydrogène consommé par heure | 11 | 24 | 39 | 58 | 80 | 106 | 136 | 171 | 212 | 259 |

## Pièges fréquents

- **Une mine de plus peut faire baisser la production totale** : sans centrale correspondante, le déficit ralentit toutes les mines.
- **La production solaire bouge dans le mois** : la température actuelle varie, et avec elle le bonus des Capteurs. Gardez une marge.
- **Les Collecteurs solaires sont vulnérables** : ils peuvent être détruits en combat, et presque tous les vaisseaux ont un tir rapide contre eux.
- **Le Réacteur coûte de l'hydrogène** : sa consommation réduit votre stock de carburant.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Liste des vaisseaux](/fr/fleet/ships)
