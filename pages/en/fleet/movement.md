---
wiki_id: 105
locale: "en"
path: "fleet/movement"
url: "https://wiki.dynastynova.com/en/fleet/movement"
title: "Fleet movement"
description: "Speed, flight time, hydrogen use and fleet slots."
tags: ["fleet"]
published: true
created: "2026-10-02T13:11:09.961Z"
updated: "2026-10-02T16:38:06.533Z"
---

# Fleet movement

> **In short**: a flight's duration depends on distance, the speed of the slowest ship and the speed percentage you choose. Its hydrogen cost depends on distance, the ships sent and speed. Flying slower costs much less.
{.is-info}

> **Universe setting**: fleet speed may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

### Fleet slots
1. The number of fleets in flight at the same time is limited: **fleet slots = 1 + Quantum Computing level**. An expedition also takes a slot.

### Speed
2. A ship's speed = base speed × (1 + bonus × level of its drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive.
3. A fleet flies at the speed of its **slowest ship**, raised by the Coordinated propulsion alliance talent.
4. You choose a **speed percentage** from 10 to 100%, in steps of 10.

### Duration
5. **Duration (seconds)** = (10 + 35000 / speed% × √(10 × distance / V)) / universe fleet speed, rounded, minimum 1 second. V is the fleet's speed, speed% the chosen percentage.
6. Distance is computed from the coordinates (see [Coordinates](/en/universe/coordinates)).

### Hydrogen use
7. **Use per trip** = sum, for each ship type, of: fuel use × number × distance / 35,000 × (speed% / 100 × √(fleet V / ship V) + 1)², rounded down, minimum 1.
8. A ship faster than the rest of its fleet uses less.
9. **The return trip is paid at departure** (outbound and return charged together) for every mission except **Colonization** and **Stationing**.
10. The Optimised supply alliance talent removes 5% per level. No research lowers a ship's fuel use.

### Recall
11. A fleet can be **recalled at any time before the end of its outbound trip**. Recalling charges nothing more and **refunds no** hydrogen.

## Worked example

10 Interceptors (speed 20,000 with Combustion Drive 6, fuel use 20 each) attack from [2:40:8] to [2:50:3]. Distance: 2,700 + 95 × 10 = **3,650**.

| Speed | One-way duration                                                        | One-way hydrogen                              | Charged at departure (round trip) |
|---|-------------------------------------------------------------------------|-----------------------------------------------|---|
| 100% | 10 + (35000/10) × √(10 × 3650 / 20000) ≈ **4738 s** (1 hour 18 min 8 s) | 20 × 10 × 3650 / 3500 × (1 + 1)² ≈ **208**    | **166** |
| 50% | 10 + (35000/5) × √1.825 ≈ **9466 s** (2 hours 37 min 46 s)              | 20 × 10 × 3,650 / 35,000 × (0.5 + 1)² ≈ **46** | **92** |

At half speed, the flight takes twice as long but uses **45% less hydrogen**.

## Detailed data

### Drives

| Drive | Bonus per level | Ships |
|---|---|---|
| Combustion Drive | +10% | Cargo Shuttle, Stellar Freighter, Salvager, Scout, Interceptor |
| Impulse Drive | +20% | Space Pioneer, Assailant, Corvette, Orbital Striker |
| Hyperspace Drive | +30% | Battleship, Predator, Annihilator, Stellar Colossus |

Base speeds and fuel use are on the [Ships list](/en/fleet/ships) page.

## Common pitfalls

- **The slowest sets the pace**: a single Salvager (speed 2,000) slows a whole fleet of Interceptors.
- **The return is paid at departure**: plan hydrogen for the round trip before attacking.
- **Recalling refunds nothing**: the hydrogen spent is lost.
- **Quantum Computing caps your fleets**: at level 2, only 3 fleets in flight, expeditions included.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Missions](/en/fleet/missions)
- [Ships list](/en/fleet/ships)
- [Expeditions](/en/fleet/expeditions)
- [Alliance missions and station](/en/players/alliance-missions)
