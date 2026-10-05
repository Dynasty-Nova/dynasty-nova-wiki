---
wiki_id: 44
locale: "fr"
path: "combat/how-combat-works"
url: "https://wiki.dynastynova.com/fr/combat/how-combat-works"
title: "Déroulement d'un combat"
description: "Rounds, tirs, boucliers, explosions et résultat."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:10.079Z"
updated: "2026-10-02T16:36:45.627Z"
---

# Déroulement d'un combat

> **En bref** : un combat dure au plus 6 rounds. À chaque round, les boucliers se rechargent, l'attaquant tire, puis le défenseur. Chaque tir vise une unité adverse au hasard et touche toujours. Un tir trop faible rebondit sur les boucliers ; un tir qui entame la coque peut faire exploser sa cible.
{.is-info}

## Règles

### Statistiques de combat
1. **Attaque** = attaque de base × (1 + 0,1 × Systèmes Offensifs).
2. **Bouclier** = bouclier de base × (1 + 0,1 × Champs de Protection).
3. **Coque** = structure × (1 + 0,1 × Métallurgie Avancée) / 10.
4. Les talents d'alliance Doctrine d'armement et Doctrine de protection ajoutent 5 %.

### Déroulement d'un round
5. Un combat compte **6 rounds au plus**. Il s'arrête dès qu'un camp n'a plus d'unité.
6. Au début de chaque round, **tous les boucliers se rechargent** entièrement et les effectifs sont figés.
7. **L'attaquant tire, puis le défenseur.** Une unité vivante au début du round tire toutes ses salves, même si elle est détruite pendant le round : en pratique, les tirs sont simultanés.
8. Chaque tir vise une **unité adverse tirée au hasard** parmi les unités vivantes. **Tout tir touche.**
9. Après un tir, un vaisseau qui a un [tir rapide](/fr/fleet/rapid-fire) contre sa cible peut tirer à nouveau.

### Dégâts
10. **Règle du 1 %** : un tir inférieur à 1 % du bouclier maximal de la cible **rebondit** sans aucun effet.
11. Sinon, le **bouclier absorbe** les dégâts tant qu'il en reste, et l'excédent passe entièrement sur la **coque**.
12. **Explosion** : après un tir qui entame la coque sans la détruire, si la coque passe sous 70 %, l'unité explose avec une probabilité égale à **1 − part de coque restante**. Un tir qui rebondit ne déclenche pas ce tirage.

### Résultat
13. **Victoire de l'attaquant** si le défenseur n'a plus d'unité ; **victoire du défenseur** si l'attaquant n'a plus d'unité ; sinon **égalité** (les deux camps encore debout après 6 rounds, ou les deux détruits).
14. Le pillage n'a lieu qu'en cas de victoire de l'attaquant.
15. Chaque combat est **déterministe** : rejoué, il donne exactement le même résultat.

## Exemple chiffré

**Un Cuirassé (attaque 1 000) tire sur un Intercepteur** (bouclier 10, coque 400, sans recherche)
- Le bouclier absorbe 10, la coque prend 990 : l'Intercepteur est **détruit**.

**4 Intercepteurs (attaque 50) tirent sur un Cuirassé** (bouclier 200, coque 6 000)
- Seuil du 1 % : 2. Les tirs passent.
- Les 4 tirs (200 au total) vident le bouclier, **sans toucher la coque**. Au round suivant, le bouclier est de nouveau plein.

**Une unité dont la coque tombe à 60 %**
- Chance d'exploser : 1 − 0,60 = **40 %**.

## Pièges fréquents

- **Les petits tirs s'écrasent sur les boucliers** : des unités faibles en nombre peuvent ne jamais entamer la coque d'une grosse cible, puisque les boucliers se rechargent à chaque round.
- **La cible est aléatoire** : vous ne choisissez pas ce que vos vaisseaux visent. Les unités nombreuses et bon marché absorbent beaucoup de tirs.
- **6 rounds, pas plus** : si personne n'est éliminé, c'est une égalité et l'attaquant ne pille rien.
- **Les défenses tirent aussi** : chaque défense tire une fois par round, sans tir rapide.

## Pages liées

- [Tirs rapides](/fr/fleet/rapid-fire)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Pillage](/fr/combat/plunder)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Simulateur de combat](/fr/combat/simulator)
