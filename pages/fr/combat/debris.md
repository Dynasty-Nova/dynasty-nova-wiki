---
wiki_id: 47
locale: "fr"
path: "combat/debris"
url: "https://wiki.dynastynova.com/fr/combat/debris"
title: "Champs de ruines (débris)"
description: "Débris créés par les combats, recyclage et formation des lunes."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:15.769Z"
updated: "2026-10-02T17:40:36.847Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Champs de ruines (débris)

> **En bref** : quand des vaisseaux sont détruits, 30 % de leur métal et de leur cristal forment un champ de ruines en orbite. Ces débris ne disparaissent jamais : il faut les recycler avec des Récupérateurs. Un gros champ de ruines peut aussi faire naître une lune.
{.is-info}

> **Paramètre d'univers** : le taux de débris des vaisseaux et des défenses, ainsi que la chance et le seuil de formation des lunes, peuvent être différents selon l'univers.
> Par défaut et sur Redline : vaisseaux **30 %**, défenses **0 %**, lune **20 % maximum pour 2 000 000 de débris**
{.is-info}

<img src="/images/illustrations/ships/recuperateur.jpg" width="180" alt="Récupérateur">

## Règles

1. Les vaisseaux détruits **des deux camps**, civils compris, laissent **30 %** de leur coût en **métal et cristal**. L'hydrogène ne laisse rien.
2. Les **défenses** détruites ne laissent **aucun débris**.
3. Les combats contre les pirates et aliens d'expédition laissent **10 %**.
4. Les débris **ne disparaissent jamais**. Seul le recyclage les retire. Ils restent même si la planète en dessous disparaît.
5. Pour les récupérer, envoyez des **Récupérateurs** en mission **Recyclage**. La récolte est limitée par la soute de la flotte : ce qui ne rentre pas reste en orbite.
6. **Formation d'une lune** : après un combat, la chance qu'une lune se forme est de **1 % par tranche de 100 000 débris**, avec un maximum de **20 %** (atteint à 2 000 000 de débris). La formation ne consomme pas les débris.
7. La destruction d'une lune ne laisse aucun débris.

## Exemple chiffré

Vous détruisez 100 Intercepteurs (3 000 métal et 1 000 cristal chacun) :
- Débris : 30 % × 300 000 métal = **90 000 métal**, et 30 % × 100 000 cristal = **30 000 cristal**.
- Récolte totale : 120 000 ressources. Un Récupérateur emporte 20 000 : il en faut **6** (sans bonus de Pliage Spatial).
- Chance de former une lune : 120 000 / 100 000 = **1,2 %**.

## Données détaillées

| Source | Part en débris |
|---|---|
| Vaisseau détruit (attaquant ou défenseur) | 30 % du métal et du cristal |
| Défense détruite | 0 % |
| Combat d'expédition (pirates, aliens) | 10 % |
| Destruction de lune | rien |

| Débris du combat | 100 000 | 500 000 | 1 000 000 | 2 000 000 et plus |
|---|---|---|---|---|
| Chance de lune | 1 % | 5 % | 10 % | 20 % |

## Pièges fréquents

- **Vos propres pertes nourrissent le champ** : un combat perdu en défense laisse aussi des débris au-dessus de votre planète, que d'autres peuvent recycler.
- **Pliage Spatial augmente la soute** : +5 % par niveau, utile pour recycler avec moins de Récupérateurs.
- **Les défenses ne rapportent rien** : seules les flottes détruites créent des débris.
- **Le premier arrivé se sert** : le champ appartient à celui qui le recycle.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Les lunes](/fr/universe/moons)
- [Station de réparation](/fr/economy/repair-station)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
