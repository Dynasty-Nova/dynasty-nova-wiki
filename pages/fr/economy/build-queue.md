---
wiki_id: 23
locale: "fr"
path: "economy/build-queue"
url: "https://wiki.dynastynova.com/fr/economy/build-queue"
title: "Files de construction"
description: "Ordres en file, paiement et annulation."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:29.825Z"
updated: "2026-10-02T16:36:16.412Z"
---

# Files de construction

> **En bref** : chaque planète a quatre files : bâtiments, recherche, vaisseaux et défenses. Chaque file accepte 2 ordres (5 en Premium), celui en cours compris. Un bâtiment ou une recherche n'est payé qu'au moment où il démarre ; s'il ne peut pas être payé, il est abandonné sans frais.
{.is-info}

> **Paramètre d'univers** : la taille des files peut être différente selon l'univers.
> Par défaut et sur Redline : **2 ordres**, **5 en Premium**
{.is-info}

## Règles

1. Quatre files indépendantes : **bâtiments**, **recherche**, **vaisseaux**, **défenses**.
2. Chaque file accepte **2 ordres**, celui en cours compris, ou **5 en Premium**.
3. Un **bâtiment** ou une **recherche** est **payé au lancement**, pas à la mise en file. Si, au moment de démarrer, la planète n'a pas les ressources, l'ordre est **abandonné sans frais**.
4. Les ordres en attente affichent une **durée estimée**, recalculée au lancement.
5. On ne peut pas mettre en file une amélioration et une démolition du même bâtiment en même temps.
6. Pendant que le **Dock orbital** produit des unités, il ne peut être ni amélioré ni démoli. Pendant que le **Centre d'innovation** est en travaux, aucune recherche ne peut être lancée ni ajoutée.

### Annulation
7. Annuler un ordre **encore en attente** ne coûte rien et ne rend rien : il n'a pas été payé.
8. Annuler un **bâtiment ou une recherche en cours** rend **80 % du coût × (temps restant / durée totale)**, arrondi à l'inférieur pour chaque ressource.
9. Annuler une commande de **vaisseaux ou de défenses** rend 80 % des unités payées mais pas encore livrées, sans prorata de temps. Les unités déjà livrées sont conservées.
10. L'**énergie requise** n'est jamais remboursée : elle n'est pas dépensée.

## Exemple chiffré

Vous annulez un bâtiment qui coûtait 20 000 métal et 10 000 cristal, alors que 25 % de son temps est écoulé.
- Temps restant : 75 %.
- Remboursement : 80 % × 75 % = **60 %**, soit **12 000 métal et 6 000 cristal**.
- Vous perdez 8 000 métal et 4 000 cristal : annuler tôt coûte déjà 20 %.

## Pièges fréquents

- **Une annulation n'est jamais gratuite** : même juste après le lancement, vous perdez au moins 20 %.
- **Gardez les ressources pour l'ordre suivant** : un ordre qui ne peut pas être payé à son tour est abandonné.
- **Le Premium allonge les quatre files** : bâtiments, recherche, vaisseaux et défenses passent tous à 5 ordres.

## Pages liées

- [Liste des bâtiments](/fr/economy/buildings)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Premium, boutique et Points stellaires](/fr/misc/premium)
