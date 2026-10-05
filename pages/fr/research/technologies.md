---
wiki_id: 28
locale: "fr"
path: "research/technologies"
url: "https://wiki.dynastynova.com/fr/research/technologies"
title: "Liste des technologies"
description: "Toutes les technologies : effets, niveaux maximum, prérequis."
tags: ["research"]
published: true
created: "2026-10-02T13:08:39.261Z"
updated: "2026-10-02T17:40:12.608Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des technologies

> **En bref** : les 17 technologies se recherchent au Centre d'innovation. Elles débloquent bâtiments, vaisseaux et défenses, et apportent des bonus permanents à tout votre empire : production, vitesse, combat, espionnage, colonies, emplacements de flotte. Un niveau de recherche vaut pour toutes vos planètes.
{.is-info}

> **Paramètre d'univers** : la vitesse de recherche peut être différente selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

1. Une recherche se lance depuis une planète équipée d'un **Centre d'innovation**. Elle est **payée au lancement**.
2. Un niveau acquis profite à **toutes vos planètes**.
3. **Durée** d'une recherche (en heures) = (métal + cristal du niveau) / (1 000 × (1 + niveau effectif du Centre d'innovation)), divisée par la vitesse recherche de l'univers.
4. Le **niveau effectif** est celui du Centre d'innovation de la planète, augmenté des Centres mis en réseau par la [Collaboration Stellaire](/fr/research/stellar-collaboration).
5. **Points** : 1 point par tranche de 1 000 ressources dépensées, comptés dans les points de recherche.
6. Chaque technologie a un **niveau maximum**.

## Exemple chiffré

Renseignement Tactique niveau 4, lancé depuis une planète dont le Centre d'innovation est au niveau 4 :
- Coût : 1 600 métal, 8 000 cristal, 1 600 hydrogène.
- Durée : (1 600 + 8 000) / (1 000 × (1 + 4)) = 1,92 h, soit **1 h 55 min 12 s**.
- Points de recherche gagnés : (1 600 + 8 000 + 1 600) / 1 000 = **11,2**.

## Données détaillées

### Effets

| Technologie | Effet |
|---|---|
| <img src="/images/illustrations/research/science-energetique.jpg" width="48" alt="Science Énergétique"> Science Énergétique | Augmente la production du Réacteur thermonucléaire. Prérequis de nombreuses technologies. |
| <img src="/images/illustrations/research/maitrise-du-plasma.jpg" width="48" alt="Maîtrise du Plasma"> Maîtrise du Plasma | Augmente la production de métal et de cristal (exemple relevé : +13 métal/h et +5 cristal/h au niveau 1, sur une planète avec Excavateur minéral 13 et Extracteur cristallin 13). |
| <img src="/images/illustrations/research/calcul-quantique.jpg" width="48" alt="Calcul Quantique"> Calcul Quantique | Emplacements de flotte = 1 + niveau. Une expédition occupe aussi un emplacement. |
| <img src="/images/illustrations/research/collaboration-stellaire.jpg" width="48" alt="Collaboration Stellaire"> Collaboration Stellaire | Met en réseau vos Centres d'innovation pour accélérer la recherche. |
| <img src="/images/illustrations/research/diplomatie-stellaire.jpg" width="48" alt="Diplomatie Stellaire"> Diplomatie Stellaire | Capacité de l'alliance que vous fondez (voir ci-dessous). Niveau 1 requis pour fonder une alliance. |
| <img src="/images/illustrations/research/propulseur-chimique.jpg" width="48" alt="Propulseur Chimique"> Propulseur Chimique | +10 % de vitesse par niveau pour les vaisseaux équipés de ce moteur. |
| <img src="/images/illustrations/research/moteur-magnetique.jpg" width="48" alt="Moteur Magnétique"> Moteur Magnétique | +20 % de vitesse par niveau pour les vaisseaux équipés de ce moteur. |
| <img src="/images/illustrations/research/navigation-transdimensionnelle.jpg" width="48" alt="Navigation Transdimensionnelle"> Navigation Transdimensionnelle | +30 % de vitesse par niveau pour les vaisseaux équipés de ce moteur. |
| <img src="/images/illustrations/research/systemes-photoniques.jpg" width="48" alt="Systèmes Photoniques"> Systèmes Photoniques | Prérequis de défenses, de vaisseaux et d'autres technologies. |
| <img src="/images/illustrations/research/manipulation-ionique.jpg" width="48" alt="Manipulation Ionique"> Manipulation Ionique | Prérequis de défenses, de vaisseaux et d'autres technologies. |
| <img src="/images/illustrations/research/pliage-spatial.jpg" width="48" alt="Pliage Spatial"> Pliage Spatial | +5 % de capacité de soute par niveau (transport, pillage, recyclage, trouvailles d'expédition). Niveau 7 requis pour la Porte de saut. |
| <img src="/images/illustrations/research/systemes-offensifs.jpg" width="48" alt="Systèmes Offensifs"> Systèmes Offensifs | +10 % d'attaque par niveau (vaisseaux et défenses). |
| <img src="/images/illustrations/research/champs-de-protection.jpg" width="48" alt="Champs de Protection"> Champs de Protection | +10 % de bouclier par niveau (vaisseaux et défenses). |
| <img src="/images/illustrations/research/metallurgie-avancee.jpg" width="48" alt="Métallurgie Avancée"> Métallurgie Avancée | +10 % de structure par niveau (vaisseaux et défenses). |
| <img src="/images/illustrations/research/manipulation-gravitationnelle.jpg" width="48" alt="Manipulation Gravitationnelle"> Manipulation Gravitationnelle | Prérequis du Colossus stellaire. Se paie en énergie et ne prend aucun temps. |
| <img src="/images/illustrations/research/renseignement-tactique.jpg" width="48" alt="Renseignement Tactique"> Renseignement Tactique | Détail des rapports d'espionnage et contre-espionnage ; −5 % par niveau sur l'hydrogène des missions d'espionnage (jusqu'à −50 %) ; au niveau 10, une case espionnée reste découverte durablement. |
| <img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="48" alt="Cosmologie Appliquée"> Cosmologie Appliquée | Nombre de planètes, expéditions simultanées et durée maximale des expéditions (voir ci-dessous). |

### Cosmologie Appliquée

| Niveau | 0 | 1 | 3 | 4 | 5 | 7 | 9 | 16 |
|---|---|---|---|---|---|---|---|---|
| Planètes au total (planète mère comprise) | 1 | 2 | 3 | 3 | 4 | 5 | 6 | 9 |
| Expéditions simultanées | 0 | 1 | 1 | 2 | 2 | 2 | 3 | 4 |
| Durée maximale d'une expédition | | 1 h | 3 h | 4 h | 5 h | 7 h | 9 h | 16 h |

Planètes au total = 1 + partie entière((niveau + 1) / 2). Expéditions simultanées = partie entière(√niveau).

### Diplomatie Stellaire

| Niveau du fondateur | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Membres de l'alliance | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 50 |

Une capacité acquise ne redescend jamais. Le talent d'alliance Ambassades ajoute jusqu'à 6 sièges.

### Niveau maximum, prérequis et coût relevé

| Technologie | Niveau max | Prérequis | Coût relevé (niveau) |
|---|---|---|---|
| Science Énergétique | 25 | Centre d'innovation 1 | 0 / 3 200 / 1 600 (niv. 3) |
| Maîtrise du Plasma | 20 | Centre d'innovation 4, Science Énergétique 8, Systèmes Photoniques 10, Manipulation Ionique 5 | 2 000 / 4 000 / 1 000 (niv. 1) |
| Calcul Quantique | 20 | Centre d'innovation 1 | 0 / 800 / 1 200 (niv. 2) |
| Collaboration Stellaire | 10 | Centre d'innovation 10, Calcul Quantique 8, Pliage Spatial 8 | 240 000 / 400 000 / 160 000 (niv. 1) |
| Diplomatie Stellaire | 8 | Centre d'innovation 5, Calcul Quantique 4 | 5 000 / 10 000 / 5 000 (niv. 1) |
| Propulseur Chimique | 15 | Centre d'innovation 1, Science Énergétique 1 | 12 800 / 0 / 19 200 (niv. 6) |
| Moteur Magnétique | 15 | Centre d'innovation 2, Science Énergétique 1, Propulseur Chimique 3 | 2 000 / 4 000 / 600 (niv. 1) |
| Navigation Transdimensionnelle | 15 | Centre d'innovation 7, Science Énergétique 1, Pliage Spatial 3 | 10 000 / 20 000 / 6 000 (niv. 1) |
| Systèmes Photoniques | 20 | Centre d'innovation 1, Science Énergétique 2 | 3 200 / 1 600 / 0 (niv. 5) |
| Manipulation Ionique | 15 | Centre d'innovation 4, Science Énergétique 4, Systèmes Photoniques 5 | 1 000 / 300 / 100 (niv. 1) |
| Pliage Spatial | 15 | Centre d'innovation 7, Science Énergétique 5, Systèmes Photoniques 7, Manipulation Ionique 5 | 0 / 4 000 / 2 000 (niv. 1) |
| Systèmes Offensifs | 20 | Centre d'innovation 4 | 1 600 / 400 / 0 (niv. 2) |
| Champs de Protection | 20 | Centre d'innovation 6, Science Énergétique 3 | 200 / 600 / 0 (niv. 1) |
| Métallurgie Avancée | 20 | Centre d'innovation 2 | 4 000 / 0 / 0 (niv. 3) |
| Manipulation Gravitationnelle | 10 | Centre d'innovation 12, Science Énergétique 12, Systèmes Photoniques 12, Manipulation Ionique 8 | 300 000 énergie (niv. 1) |
| Renseignement Tactique | 15 | Centre d'innovation 3 | 1 600 / 8 000 / 1 600 (niv. 4) |
| Cosmologie Appliquée | 20 | Centre d'innovation 3, Renseignement Tactique 4, Moteur Magnétique 3 | 4 000 / 8 000 / 4 000 (niv. 1) |

Coûts en métal / cristal / hydrogène, relevés en jeu pour le niveau indiqué. Les tables complètes seront ajoutées sur les pages de chaque technologie.

## Pièges fréquents

- **Le Centre d'innovation compte** : la durée dépend du Centre de la planète qui lance la recherche. Lancez vos recherches depuis votre meilleur Centre.
- **Calcul Quantique limite vos flottes** : avec le niveau 2, vous ne pouvez avoir que 3 flottes en vol, expéditions comprises.
- **Une colonie de plus tous les deux niveaux** : Cosmologie Appliquée 2 ne donne pas de planète supplémentaire par rapport au niveau 1.
- **Diplomatie Stellaire est celle du fondateur** : la capacité de l'alliance dépend uniquement du niveau de son fondateur.
- **Science Énergétique n'améliore pas les Capteurs photovoltaïques** ni les Collecteurs solaires : seulement le Réacteur thermonucléaire.

## Pages liées

- [Arbre technologique](/fr/research/tech-tree)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Coloniser](/fr/universe/colonization)
- [Expéditions](/fr/fleet/expeditions)
- [Alliances](/fr/players/alliances)
