---
wiki_id: 120
locale: "en"
path: "combat/moon-destruction"
url: "https://wiki.dynastynova.com/en/combat/moon-destruction"
title: "Moon destruction"
description: "Destroying a moon with Stellar Colossi."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:40.153Z"
updated: "2026-10-02T17:40:44.582Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Moon destruction

> **In short**: a fleet made only of Stellar Colossi can try to destroy another player's moon. It must win the battle first. Then two independent rolls decide whether the moon is destroyed and whether the Colossi are lost.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Stellar Colossus">

## Rules

1. The **Moon destruction** mission requires a fleet made **only of Stellar Colossi**, and targets another player's moon.
2. A **regular battle** takes place first, against the moon's fleet and defenses.
3. The rolls only happen on a **clear victory** for the attacker.
4. With **S** the moon's diameter in km and **N** the number of surviving Colossi:
   - chance to **destroy the moon** = min(100, (100 − √S) × √N)%;
   - chance to **lose the Colossi** = √S / 2%, a single roll for the whole fleet.
5. Both rolls are **independent** and both happen, whether the moon blows up or not. Sending more Colossi only improves the chance of destroying the moon: the risk of losing the fleet does not move.
6. If the moon is destroyed: everything on it disappears, and the matching points are removed from its owner. Fleets heading to or from the moon are redirected to the planet.
7. **No plunder, no debris.**
8. A moon whose owner is on vacation cannot be destroyed.

## Worked example

A **8,944 km** moon and **100** surviving Colossi:
- √8,944 ≈ 94.6.
- Chance to destroy the moon: (100 − 94.6) × √100 ≈ **54.3%**.
- Chance to lose the Colossi: 94.6 / 2 ≈ **47.3%**.

## Detailed data

Chance to destroy an 8,944 km moon by number of surviving Colossi (the loss risk stays at 47.3%):

| Surviving Colossi | 1 | 4 | 25 | 100 | 400 |
|---|---|---|---|---|---|
| Destruction chance | 5.4% | 10.9% | 27.1% | 54.3% | 100% |

## Common pitfalls

- **A big moon is harder and more dangerous**: the larger the diameter, the harder the destruction and the higher the risk of losing the fleet.
- **Numbers do not protect the fleet**: the loss risk depends only on the diameter.
- **You must win the battle first**: without a clear victory, no roll.

## Related pages

- [Moons](/en/universe/moons)
- [Ships list](/en/fleet/ships)
- [Missions](/en/fleet/missions)
- [How combat works](/en/combat/how-combat-works)
