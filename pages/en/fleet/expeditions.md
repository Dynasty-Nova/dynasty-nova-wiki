---
wiki_id: 107
locale: "en"
path: "fleet/expeditions"
url: "https://wiki.dynastynova.com/en/fleet/expeditions"
title: "Expeditions"
description: "Exploring deep space: conditions, outcomes and odds."
tags: ["fleet"]
published: true
created: "2026-10-02T13:11:13.809Z"
updated: "2026-10-02T17:41:05.921Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Expeditions

> **In short**: beyond the last position of each system lies deep space. A fleet holding position there sometimes comes back loaded with resources or abandoned ships… or runs into pirates, aliens, even a black hole. You need Astrophysics to go.
{.is-info}

> **Universe setting**: expeditions may or may not be enabled depending on the universe.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Astrophysics">

## Rules

### Setting out
1. You need at least **Astrophysics level 1**.
2. The target is the system's **deep space** (the position after the last one).
3. The fleet cannot be made **only of Scouts**: at least one other hull is required. A Scout on board is not lost and tells you the state of the area.
4. You choose the **time on site**: from 1 hour up to as many hours as your Astrophysics level.
5. **Simultaneous expeditions** = whole part of √(Astrophysics level): 1 at level 1, 2 at level 4, 3 at level 9, 4 at level 16. Each expedition also takes a fleet slot.
6. **Hydrogen**: outbound, return and every hour on site are paid at departure. Holding position costs ceiling(hours × total fuel use / 10) and must fit in the holds along with the cargo.

### Outcomes
7. **Time on site does not change the odds**.
8. An over-visited area **wears out**: from 10 expeditions completed on the same cell within 24 hours, find chances are multiplied by 0.75; from 25, by 0.5. The rest goes to "nothing".
9. **Resources**: metal in 50% of cases, crystal in 33%, hydrogen in 17%. The find is capped by free cargo space: the surplus is lost.
10. **Ships**: abandoned ships join your fleet, up to one rank above your best ship on board. Never a Stellar Colossus, Space Pioneer, Salvager or Solar Collector.
11. **Delay** or **early return**: the return trip is lengthened or shortened.
12. **Pirates** and **aliens**: a real battle against a fleet proportional to yours. Pirates have your technologies minus 3 levels, aliens plus 3. Debris from these battles (10%) stays on the cell. No plunder.
13. **Black hole**: the whole fleet is lost.

### Size of finds
14. The bigger your fleet, the more it brings back: **expedition points** = max(200, total fleet structure / 200), capped according to the points of the universe's **best player**.
15. The size rolled multiplies these points: normal (89%, factor 10 to 50), large (10%, 50 to 100), huge (1%, 100 to 200).
16. Resources found = factor × points, in metal equivalent: the amount is divided by 2 for crystal and by 3 for hydrogen. Ships found: budget = factor × points / 2.

## Worked example

A fleet of 50 Stellar Freighters (structure 12,000 each) sets out in a universe whose best player has 500,000 points.
- Total structure: 600,000. Expedition points: 600,000 / 200 = **3,000**.
- Cap for a best player under 1,000,000 points: **6,000**. The 3,000 points therefore stand.
- A normal-size resource find, factor 30, in metal: 30 × 3,000 = **90,000 metal**. In crystal it would be 45,000; in hydrogen, 30,000.
- The 50 Freighters carry 1,250,000: plenty of room.

## Detailed data

### Odds

| Outcome | Probability |
|---|---|
| Resources | 33% |
| Nothing | 33% |
| Ships | 17% |
| Delay | 7% |
| Pirates | 5.5% |
| Aliens | 2.3% |
| Early return | 2% |
| Black hole | 0.2% |

### Delay and early return

| Size | Normal | Large | Huge |
|---|---|---|---|
| Delay: return lengthened by | time on site × 2 | × 3 | × 5 |
| Early return: return divided by | 2 | 3 | 5 |

### Pirates and aliens: enemy strength

| Size | Normal | Large | Huge |
|---|---|---|---|
| Pirates (as % of your fleet) | 30% | 50% | 80% |
| Aliens (as % of your fleet) | 40% | 60% | 90% |

A fixed escort is added to these fleets.

### Expedition points cap

| Best player's points | Cap |
|---|---|
| under 10,000 | 200 |
| under 100,000 | 2,500 |
| under 1,000,000 | 6,000 |
| under 5,000,000 | 9,000 |
| under 25,000,000 | 12,000 |
| under 50,000,000 | 15,000 |
| under 75,000,000 | 18,000 |
| under 100,000,000 | 21,000 |
| 100,000,000 or more | 25,000 |

## Common pitfalls

- **Staying longer does not help** your odds: choose the duration to fit your schedule, not to "raise the chance".
- **Bring cargo space**: a find that does not fit is lost.
- **Change areas**: a heavily visited cell wears out.
- **The black hole is real**: a 0.2% chance of losing everything. Do not send your main fleet.

## Related pages

- [Missions](/en/fleet/missions)
- [Fleet movement](/en/fleet/movement)
- [Technologies list](/en/research/technologies)
- [Coordinates](/en/universe/coordinates)
- [Debris fields](/en/combat/debris)
