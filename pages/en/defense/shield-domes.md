---
wiki_id: 111
locale: "en"
path: "defense/shield-domes"
url: "https://wiki.dynastynova.com/en/defense/shield-domes"
title: "Defensive Barrier and Protective Dome"
description: "The two planetary shields."
tags: ["defense"]
published: true
created: "2026-10-02T13:11:21.637Z"
updated: "2026-10-02T17:40:32.442Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Defensive Barrier and Protective Dome

> **In short**: the Defensive Barrier and the Protective Dome are defenses with a very large shield, limited to one of each per planet. They absorb shots for themselves only: they do not protect other units.
{.is-info}

<img src="/images/illustrations/defense/barriere-defensive.jpg" width="180" alt="Defensive Barrier"> <img src="/images/illustrations/defense/dome-protecteur.jpg" width="180" alt="Protective Dome">

## Rules

1. **One of each** per planet: you cannot order or queue a second one while the first exists.
2. In combat, they are **ordinary targets** with a large individual shield. They **do not create a global shield** around the planet.
3. Like any defense, they have a **70% chance** of being repaired after being destroyed, and a 30% chance of being lost for good. You can then build a new one.
4. They barely fire (attack 1): their role is to soak up shots.
5. Destroyed by Long-Range Warheads, they are lost for good. Without a designated target, Warheads hit the toughest defense first: often the Dome.

## Worked example

A Protective Dome (shield 10,000, hull 10,000) against Interceptors (attack 50):
- 1% threshold: 100. An attack of 50 is below it: **every shot bounces**, the Dome loses nothing.
- Against Battleships (attack 1,000), shots get through: 10 shots empty the shield, the next ones damage the hull.

## Detailed data

| | Defensive Barrier | Protective Dome |
|---|---|---|
| Cost | 10,000 metal, 10,000 crystal | 50,000 metal, 50,000 crystal |
| Structure | 20,000 | 100,000 |
| Combat hull | 2,000 | 10,000 |
| Shield | 2,000 | 10,000 |
| Attack | 1 | 1 |
| Requirements | Orbital Dock 1, Shielding Technology 2 | Orbital Dock 6, Shielding Technology 6 |
| Copies | 1 | 1 |

## Common pitfalls

- **No protective bubble**: your other defenses and ships stay exposed.
- **The Dome draws Warheads**: it is often the toughest defense, so the first hit by a salvo with no designated target.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
- [How combat works](/en/combat/how-combat-works)
- [Defense rebuild](/en/combat/defense-rebuild)
