---
wiki_id: 37
locale: "fr"
path: "fleet/expeditions"
url: "https://wiki.dynastynova.com/fr/fleet/expeditions"
title: "Expéditions"
description: "Explorer l'espace lointain : conditions, résultats et probabilités."
tags: ["fleet"]
published: true
created: "2026-10-02T13:08:56.440Z"
updated: "2026-10-02T17:41:04.333Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Expéditions

> **En bref** : au-delà de la dernière position de chaque système s'étend l'espace lointain. Une flotte qui y tient sa position revient parfois chargée de ressources ou de vaisseaux abandonnés… ou tombe sur des pirates, des aliens, voire un trou noir. Il faut la Cosmologie Appliquée pour partir.
{.is-info}

> **Paramètre d'univers** : les expéditions peuvent être activées ou non selon l'univers.
{.is-info}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Cosmologie Appliquée">

## Règles

### Partir
1. Il faut **Cosmologie Appliquée niveau 1** au minimum.
2. La cible est l'**espace lointain** du système (la position qui suit la dernière).
3. La flotte ne peut pas être composée **uniquement d'Éclaireurs** : il faut au moins une autre coque. Un Éclaireur embarqué n'est pas perdu et vous indique l'état de la zone.
4. Vous choisissez la **durée sur place** : de 1 heure jusqu'à autant d'heures que votre niveau de Cosmologie Appliquée.
5. **Expéditions simultanées** = partie entière(√ niveau de Cosmologie Appliquée) : 1 au niveau 1, 2 au niveau 4, 3 au niveau 9, 4 au niveau 16. Chaque expédition occupe aussi un emplacement de flotte.
6. **Hydrogène** : l'aller, le retour et chaque heure sur place sont payés au départ. Le maintien coûte plafond(heures × somme des consommations / 10) et doit tenir dans la soute avec la cargaison.

### Résultats
7. La **durée sur place ne change pas les chances**.
8. Une zone trop visitée **s'épuise** : à partir de 10 expéditions terminées sur la même case en 24 heures, les chances de trouvaille sont multipliées par 0,75 ; à partir de 25, par 0,5. Le reste va au résultat « rien ».
9. **Ressources** : métal dans 50 % des cas, cristal dans 33 %, hydrogène dans 17 %. La trouvaille est limitée par la soute libre : le surplus est perdu.
10. **Vaisseaux** : des vaisseaux abandonnés rejoignent votre flotte, jusqu'à un rang au-dessus de votre meilleur vaisseau à bord. Jamais de Colossus stellaire, de Pionnier spatial, de Récupérateur ni de Collecteur solaire.
11. **Retard** ou **retour anticipé** : le retour est allongé ou raccourci.
12. **Pirates** et **aliens** : un vrai combat contre une flotte proportionnelle à la vôtre. Les pirates ont vos technologies moins 3 niveaux, les aliens plus 3. Les débris de ces combats (10 %) restent sur la case. Pas de pillage.
13. **Trou noir** : la flotte entière est perdue.

### Taille des trouvailles
14. Plus votre flotte est grande, plus elle rapporte : **points d'expédition** = max(200, structure totale de la flotte / 200), plafonnés selon les points du **meilleur joueur** de l'univers.
15. La taille tirée multiplie ces points : normale (89 %, facteur 10 à 50), grande (10 %, 50 à 100), énorme (1 %, 100 à 200).
16. Ressources trouvées = facteur × points, en équivalent métal : le montant est divisé par 2 pour le cristal et par 3 pour l'hydrogène. Vaisseaux trouvés : budget = facteur × points / 2.

## Exemple chiffré

Une flotte de 50 Cargos stellaires (structure 12 000 chacun) part dans un univers où le meilleur joueur a 500 000 points.
- Structure totale : 600 000. Points d'expédition : 600 000 / 200 = **3 000**.
- Plafond pour un meilleur joueur sous 1 000 000 points : **6 000**. Les 3 000 points restent donc valables.
- Une trouvaille de ressources de taille normale, facteur 30, en métal : 30 × 3 000 = **90 000 métal**. En cristal, ce serait 45 000 ; en hydrogène, 30 000.
- Les 50 Cargos emportent 1 250 000 : la soute suffit largement.

## Données détaillées

### Probabilités

| Résultat | Probabilité |
|---|---|
| Ressources | 33 % |
| Rien | 33 % |
| Vaisseaux | 17 % |
| Retard | 7 % |
| Pirates | 5,5 % |
| Aliens | 2,3 % |
| Retour anticipé | 2 % |
| Trou noir | 0,2 % |

### Retard et retour anticipé

| Taille | Normale | Grande | Énorme |
|---|---|---|---|
| Retard : retour allongé de | durée sur place × 2 | × 3 | × 5 |
| Retour anticipé : retour divisé par | 2 | 3 | 5 |

### Pirates et aliens : force adverse

| Taille | Normale | Grande | Énorme |
|---|---|---|---|
| Pirates (en % de votre flotte) | 30 % | 50 % | 80 % |
| Aliens (en % de votre flotte) | 40 % | 60 % | 90 % |

Une escorte fixe s'ajoute à ces flottes.

### Plafond des points d'expédition

| Points du meilleur joueur | Plafond |
|---|---|
| moins de 10 000 | 200 |
| moins de 100 000 | 2 500 |
| moins de 1 000 000 | 6 000 |
| moins de 5 000 000 | 9 000 |
| moins de 25 000 000 | 12 000 |
| moins de 50 000 000 | 15 000 |
| moins de 75 000 000 | 18 000 |
| moins de 100 000 000 | 21 000 |
| 100 000 000 ou plus | 25 000 |

## Pièges fréquents

- **Rester plus longtemps ne sert à rien** pour les chances : choisissez la durée selon votre emploi du temps, pas pour « augmenter la chance ».
- **Prévoyez de la soute** : une trouvaille qui ne rentre pas est perdue.
- **Changez de zone** : une case très fréquentée s'épuise.
- **Le trou noir existe** : 0,2 % de chances de tout perdre. N'envoyez pas votre flotte principale.

## Pages liées

- [Les missions](/fr/fleet/missions)
- [Déplacements](/fr/fleet/movement)
- [Liste des technologies](/fr/research/technologies)
- [Coordonnées](/fr/universe/coordinates)
- [Champs de ruines](/fr/combat/debris)
