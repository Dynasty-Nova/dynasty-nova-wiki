---
wiki_id: 98
locale: "en"
path: "research/technologies"
url: "https://wiki.dynastynova.com/en/research/technologies"
title: "Technologies list"
description: "All technologies: effects, maximum levels, requirements."
tags: ["research"]
published: true
created: "2026-10-02T13:10:56.114Z"
updated: "2026-10-02T17:40:14.225Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Technologies list

> **In short**: the 17 technologies are researched at the Innovation Center. They unlock buildings, ships and defenses, and give permanent bonuses to your whole empire: output, speed, combat, espionage, colonies, fleet slots. A research level applies to all your planets.
{.is-info}

> **Universe setting**: research speed may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

1. Research is started from a planet with an **Innovation Center**. It is **paid when it starts**.
2. A level you gain applies to **all your planets**.
3. **Duration** of a research (in hours) = (metal + crystal of the level) / (1,000 × (1 + effective Innovation Center level)), divided by the universe's research speed.
4. The **effective level** is the Innovation Center level of the planet, plus the Centers networked by [Stellar Collaboration](/en/research/stellar-collaboration).
5. **Points**: 1 point per 1,000 resources spent, counted as research points.
6. Every technology has a **maximum level**.

## Worked example

Espionage Technology level 4, started from a planet whose Innovation Center is level 4:
- Cost: 1,600 metal, 8,000 crystal, 1,600 hydrogen.
- Duration: (1,600 + 8,000) / (1,000 × (1 + 4)) = 1.92 h, that is **1 h 55 min 12 s**.
- Research points gained: (1,600 + 8,000 + 1,600) / 1,000 = **11.2**.

## Detailed data

### Effects

| Technology | Effect |
|---|---|
| <img src="/images/illustrations/research/science-energetique.jpg" width="48" alt="Energy Science"> Energy Science | Raises the Thermonuclear Reactor's output. Required by many technologies. |
| <img src="/images/illustrations/research/maitrise-du-plasma.jpg" width="48" alt="Plasma Technology"> Plasma Technology | Raises metal and crystal output (example seen in game: +13 metal/h and +5 crystal/h at level 1, on a planet with Mineral Excavator 13 and Crystal Extractor 13). |
| <img src="/images/illustrations/research/calcul-quantique.jpg" width="48" alt="Quantum Computing"> Quantum Computing | Fleet slots = 1 + level. An expedition also takes a slot. |
| <img src="/images/illustrations/research/collaboration-stellaire.jpg" width="48" alt="Stellar Collaboration"> Stellar Collaboration | Networks your Innovation Centers to speed up research. |
| <img src="/images/illustrations/research/diplomatie-stellaire.jpg" width="48" alt="Stellar Diplomacy"> Stellar Diplomacy | Capacity of the alliance you found (see below). Level 1 is required to found an alliance. |
| <img src="/images/illustrations/research/propulseur-chimique.jpg" width="48" alt="Combustion Drive"> Combustion Drive | +10% speed per level for ships using this drive. |
| <img src="/images/illustrations/research/moteur-magnetique.jpg" width="48" alt="Impulse Drive"> Impulse Drive | +20% speed per level for ships using this drive. |
| <img src="/images/illustrations/research/navigation-transdimensionnelle.jpg" width="48" alt="Hyperspace Drive"> Hyperspace Drive | +30% speed per level for ships using this drive. |
| <img src="/images/illustrations/research/systemes-photoniques.jpg" width="48" alt="Laser Technology"> Laser Technology | Required by defenses, ships and other technologies. |
| <img src="/images/illustrations/research/manipulation-ionique.jpg" width="48" alt="Ion Technology"> Ion Technology | Required by defenses, ships and other technologies. |
| <img src="/images/illustrations/research/pliage-spatial.jpg" width="48" alt="Hyperspace Technology"> Hyperspace Technology | +5% cargo capacity per level (transport, plunder, recycling, expedition finds). Level 7 is required for the Jump gate. |
| <img src="/images/illustrations/research/systemes-offensifs.jpg" width="48" alt="Weapon Systems"> Weapon Systems | +10% attack per level (ships and defenses). |
| <img src="/images/illustrations/research/champs-de-protection.jpg" width="48" alt="Shielding Technology"> Shielding Technology | +10% shield per level (ships and defenses). |
| <img src="/images/illustrations/research/metallurgie-avancee.jpg" width="48" alt="Armor Technology"> Armor Technology | +10% structure per level (ships and defenses). |
| <img src="/images/illustrations/research/manipulation-gravitationnelle.jpg" width="48" alt="Graviton Technology"> Graviton Technology | Required by the Stellar Colossus. Paid in energy and takes no time. |
| <img src="/images/illustrations/research/renseignement-tactique.jpg" width="48" alt="Espionage Technology"> Espionage Technology | Spy report detail and counter-espionage; −5% per level on hydrogen for spy missions (down to −50%); at level 10, a spied cell stays discovered for good. |
| <img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="48" alt="Astrophysics"> Astrophysics | Number of planets, simultaneous expeditions and maximum expedition duration (see below). |

### Astrophysics

| Level | 0 | 1 | 3 | 4 | 5 | 7 | 9 | 16 |
|---|---|---|---|---|---|---|---|---|
| Total planets (mother planet included) | 1 | 2 | 3 | 3 | 4 | 5 | 6 | 9 |
| Simultaneous expeditions | 0 | 1 | 1 | 2 | 2 | 2 | 3 | 4 |
| Maximum expedition duration | | 1 h | 3 h | 4 h | 5 h | 7 h | 9 h | 16 h |

Total planets = 1 + whole part of ((level + 1) / 2). Simultaneous expeditions = whole part of √level.

### Stellar Diplomacy

| Founder's level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Alliance members | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 50 |

A capacity once reached never goes down. The Embassies alliance talent adds up to 6 seats.

### Maximum level, requirements and recorded cost

| Technology | Max level | Requirements | Recorded cost (level) |
|---|---|---|---|
| Energy Science | 25 | Innovation Center 1 | 0 / 3,200 / 1,600 (lvl 3) |
| Plasma Technology | 20 | Innovation Center 4, Energy Science 8, Laser Technology 10, Ion Technology 5 | 2,000 / 4,000 / 1,000 (lvl 1) |
| Quantum Computing | 20 | Innovation Center 1 | 0 / 800 / 1,200 (lvl 2) |
| Stellar Collaboration | 10 | Innovation Center 10, Quantum Computing 8, Hyperspace Technology 8 | 240,000 / 400,000 / 160,000 (lvl 1) |
| Stellar Diplomacy | 8 | Innovation Center 5, Quantum Computing 4 | 5,000 / 10,000 / 5,000 (lvl 1) |
| Combustion Drive | 15 | Innovation Center 1, Energy Science 1 | 12,800 / 0 / 19,200 (lvl 6) |
| Impulse Drive | 15 | Innovation Center 2, Energy Science 1, Combustion Drive 3 | 2,000 / 4,000 / 600 (lvl 1) |
| Hyperspace Drive | 15 | Innovation Center 7, Energy Science 1, Hyperspace Technology 3 | 10,000 / 20,000 / 6,000 (lvl 1) |
| Laser Technology | 20 | Innovation Center 1, Energy Science 2 | 3,200 / 1,600 / 0 (lvl 5) |
| Ion Technology | 15 | Innovation Center 4, Energy Science 4, Laser Technology 5 | 1,000 / 300 / 100 (lvl 1) |
| Hyperspace Technology | 15 | Innovation Center 7, Energy Science 5, Laser Technology 7, Ion Technology 5 | 0 / 4,000 / 2,000 (lvl 1) |
| Weapon Systems | 20 | Innovation Center 4 | 1,600 / 400 / 0 (lvl 2) |
| Shielding Technology | 20 | Innovation Center 6, Energy Science 3 | 200 / 600 / 0 (lvl 1) |
| Armor Technology | 20 | Innovation Center 2 | 4,000 / 0 / 0 (lvl 3) |
| Graviton Technology | 10 | Innovation Center 12, Energy Science 12, Laser Technology 12, Ion Technology 8 | 300,000 energy (lvl 1) |
| Espionage Technology | 15 | Innovation Center 3 | 1,600 / 8,000 / 1,600 (lvl 4) |
| Astrophysics | 20 | Innovation Center 3, Espionage Technology 4, Impulse Drive 3 | 4,000 / 8,000 / 4,000 (lvl 1) |

Costs in metal / crystal / hydrogen, recorded in game for the level shown. Full tables will be added to each technology's own page.

## Common pitfalls

- **The Innovation Center matters**: duration depends on the Center of the planet that starts the research. Start research from your best Center.
- **Quantum Computing caps your fleets**: at level 2, you can only have 3 fleets in flight, expeditions included.
- **One more colony every two levels**: Astrophysics 2 gives no extra planet compared to level 1.
- **Stellar Diplomacy is the founder's**: alliance capacity depends only on its founder's level.
- **Energy Science does not boost Photovoltaic Sensors** or Solar Collectors: only the Thermonuclear Reactor.

## Related pages

- [Tech tree](/en/research/tech-tree)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Buildings list](/en/economy/buildings)
- [Ships list](/en/fleet/ships)
- [Colonization](/en/universe/colonization)
- [Expeditions](/en/fleet/expeditions)
- [Alliances](/en/players/alliances)
