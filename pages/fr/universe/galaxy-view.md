---
wiki_id: 12
locale: "fr"
path: "universe/galaxy-view"
url: "https://wiki.dynastynova.com/fr/universe/galaxy-view"
title: "La vue galaxie"
description: "Lire la vue galaxie, système par système."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:08.617Z"
updated: "2026-10-02T17:41:07.527Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# La vue galaxie

> **En bref** : la vue galaxie affiche un système à la fois, position par position. Pour chaque planète, vous voyez son propriétaire, son statut, ses débris, sa lune et le nombre d'attaques qu'il vous reste contre ce joueur. C'est aussi d'ici que vous espionnez d'un clic, que vous partagez une position avec votre alliance ou que vous l'ajoutez à vos favoris.
{.is-info}

![La vue galaxie en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*La vue galaxie en affichage orbites : chaque planète a son aspect, selon son type et son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

![La vue galaxie en affichage liste](/images/screenshots/french/vue-galaxie.jpg)
*En affichage liste, les positions pas encore espionnées restent illisibles. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

1. La vue galaxie montre **un système** : toutes ses positions, puis l'espace lointain.
2. **Navigation** : flèches ← / → du clavier pour changer de système, Ctrl + ← / → (⌘ sur Mac) pour changer de galaxie.
3. Deux affichages sont proposés : en **liste** ou en **orbites**.
4. **Positions masquées** : tant qu'une position n'a pas été espionnée, tout y reste caché. Une écriture exotique, illisible, remplace le nom de la planète et celui de son propriétaire. Une case illisible peut être libre ou occupée : seul l'espionnage le révèle.
5. Une position **espionnée** dévoile la planète, son propriétaire, ses points et ses **statuts**. Avec Renseignement Tactique 10, une case espionnée reste découverte durablement.
6. Le compteur **« Attaques restantes : x / 6 »** indique combien d'attaques il vous reste contre ce joueur sur la tranche de 24 h en cours.
7. Le bouton d'**espionnage rapide** envoie un Éclaireur en un clic depuis votre planète actuelle. Il faut avoir un Éclaireur disponible sur cette planète.
8. La fiche d'une case donne aussi la **taille** de la planète, ses **cases utilisées** et sa **température**.
9. Vous pouvez **partager une position** avec votre alliance : chaque membre l'ouvre dans sa propre vue galaxie. Le message reste 30 jours dans le canal.
10. Une **étoile** ajoute la position à vos **favoris**, avec une note privée facultative.

## Exemple chiffré

Vous avez déjà attaqué un joueur deux fois aujourd'hui. Sur sa ligne, le compteur affiche **« Attaques restantes : 4 / 6 »**. Après quatre autres attaques, il affichera 0 / 6 et toute nouvelle attaque sera refusée jusqu'à la fin de la tranche de 24 h.

## Données détaillées

### Statuts affichés

| Statut | Signification |
|---|---|
| Débutant protégé | Joueur protégé par l'écart de points avec vous (voir [Protection des débutants](/fr/players/beginner-protection)) |
| Nouveau joueur | Joueur dans ses 7 premiers jours, inattaquable |
| En vacances | Joueur en mode vacances : ni attaque, ni transport, ni missiles |
| Abandonnée | Planète abandonnée, qui se dégrade avant de disparaître |
| Inhabitée | Position libre, colonisable |
| Espionnée récemment | Vous avez un rapport d'espionnage récent sur cette planète |
| Champ de ruines | Débris en orbite, à recycler |

## Pièges fréquents

- **Une case illisible ne dit rien** : elle peut cacher un joueur comme être vide. Envoyez un Éclaireur avant de conclure.
- **Le compteur d'attaques est par joueur** : il compte toutes ses planètes ensemble, et les salves de missiles aussi.
- **L'espionnage rapide part de la planète sélectionnée** : sans Éclaireur sur cette planète, le bouton ne fonctionne pas.
- **Les débris sont à tout le monde** : un champ de ruines repéré dans la galaxie revient au premier qui le recycle.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Protection des débutants](/fr/players/beginner-protection)
- [Limite d'attaques](/fr/players/attack-limit)
- [Espionner](/fr/espionage/spying)
- [Vue Empire et favoris](/fr/misc/empire-and-bookmarks)
