---
wiki_id: 89
locale: "en"
path: "economy/energy"
url: "https://wiki.dynastynova.com/en/economy/energy"
title: "Energy"
description: "Producing and using energy, shortage and operating rate."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:38.606Z"
updated: "2026-10-02T17:40:50.483Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Energy

> **In short**: your mines use energy, your power plants produce it. As long as production covers consumption, everything runs at full rate. As soon as it falls short, **all** mines slow down by the same proportion. Energy cannot be stored.
{.is-info}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Photovoltaic Sensors"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Thermonuclear Reactor"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Solar Collector">

## Rules

1. **Energy sources**:
   - **Photovoltaic Sensors**: a building that produces more when the planet's current temperature is high (× (1 + current temperature / 100) when positive).
   - **Thermonuclear Reactor**: a building that produces energy by **burning hydrogen**. Its output rises with Energy Science.
   - **Solar Collector**: a ship that stays in orbit. It produces more on a hot planet, but it can be **destroyed in an attack**.
2. **Consumption**: the Mineral Excavator, the Crystal Extractor and the Hydrogen Condenser use energy, more at each level.
3. **Shortage**: if consumption exceeds production, metal, crystal and hydrogen output is reduced **by the same proportion**. An "Energy shortage" line appears in the production breakdown.
4. **Operating rate**: each mine can be set in **steps of 10%**. Lowering the rate reduces both its output and its consumption, in the same proportion.
5. Energy is **never stored**: it is computed at every moment.
6. Some buildings and technologies require an **energy threshold** to start (Repair Station, Planetary Modulator, Graviton Technology): it is a production threshold, not a cost.

## Worked example

Your planet produces **1,000** energy and your mines need **1,250**.
- Coverage: 1,000 / 1,250 = **80%**.
- All mines run at 80%: an Excavator that should produce 2,000 metal/h only produces **1,600**.
- Adding a mine level worsens the shortage: add a power plant instead.

## Detailed data

### Consumption seen in game

| Level | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Excavator or Extractor | 448 | 531 | 626 | 735 | 859 | 1,000 | 1,162 | 1,345 | 1,554 | 1,790 |

| Level | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|
| Hydrogen Condenser | 212 | 259 | 313 | 376 | 448 | 531 | 626 | 735 | 859 | 1,000 |

### Output seen in game

Photovoltaic Sensors, on a day when the current temperature was 23 °C:

| Level | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Energy | 1,104 | 1,307 | 1,541 | 1,808 | 2,113 | 2,461 | 2,858 | 3,309 | 3,822 | 4,405 |

Thermonuclear Reactor, with Energy Science 3:

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Energy produced | 32 | 69 | 113 | 163 | 220 | 285 | 359 | 444 | 539 | 647 |
| Hydrogen used per hour | 11 | 24 | 39 | 58 | 80 | 106 | 136 | 171 | 212 | 259 |

## Common pitfalls

- **One more mine can lower total output**: without a matching power plant, the shortage slows every mine.
- **Solar output moves during the month**: the current temperature changes, and the Sensors' bonus with it. Keep a margin.
- **Solar Collectors are vulnerable**: they can be destroyed in combat, and almost every ship has rapid fire against them.
- **The Reactor costs hydrogen**: its consumption eats into your fuel stock.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Planets: size, temperature, type](/en/universe/planets)
- [Ships list](/en/fleet/ships)
