---
wiki_id: 108
locale: "en"
path: "fleet/jump-gate"
url: "https://wiki.dynastynova.com/en/fleet/jump-gate"
title: "Jump gate"
description: "Moving a fleet instantly between two moons."
tags: ["fleet", "moon"]
published: true
created: "2026-10-02T13:11:15.751Z"
updated: "2026-10-02T17:40:23.324Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Jump gate

> **In short**: the Jump gate is built on a moon. It sends a fleet instantly to another of your moons fitted with a Jump gate, with no flight time and no fuel. It carries no resources, and both gates must then recharge.
{.is-info}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Jump gate">

## Rules

1. The Jump gate can be built **on a moon only**.
2. Requirements: **Lunar base 1** and **Hyperspace Technology 7**.
3. A jump links **two different moons of the same player**, each with a recharged Jump gate.
4. The jump is **instant** and uses **no hydrogen**.
5. **Hulls only**: no resources go through. Empty the cargo holds before jumping.
6. After a jump, **both gates** (departure and arrival) recharge. Recharge time depends on the gate's level.
7. A refused jump (gate recharging, moon without a gate) uses no recharge.

## Worked example

You have a level 3 Jump gate on moon A and a level 1 gate on moon B. Your fleet jumps from A to B.
- The fleet arrives on B immediately, without spending hydrogen.
- Gate A recharges in **47 minutes** (level 3), gate B in **60 minutes** (level 1).
- A new jump from B is possible only after 60 minutes.

## Detailed data

### Recharge by level

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recharge (minutes) | 60 | 53 | 47 | 41 | 36 | 31 | 27 | 23 | 19 | 17 | 14 | 13 | 11 | 10 |

### Cost

The cost doubles at each level.

| Level | Metal | Crystal | Hydrogen |
|---|---|---|---|
| 1 | 2,000,000 | 4,000,000 | 2,000,000 |
| 2 | 4,000,000 | 8,000,000 | 4,000,000 |
| 3 | 8,000,000 | 16,000,000 | 8,000,000 |
| 4 | 16,000,000 | 32,000,000 | 16,000,000 |
| 5 | 32,000,000 | 64,000,000 | 32,000,000 |

## Common pitfalls

- **Recharge hits both ends**: upgrading only the departure gate does not let you chain jumps, the arrival gate recharges at its own pace.
- **No resources**: a loaded fleet must unload its cargo first.
- **You need two moons**: a single gate is useless.

## Related pages

- [Moons](/en/universe/moons)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Fleet movement](/en/fleet/movement)
- [Technologies list](/en/research/technologies)
