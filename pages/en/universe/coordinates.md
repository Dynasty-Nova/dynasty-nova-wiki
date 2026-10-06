---
wiki_id: 81
locale: "en"
path: "universe/coordinates"
url: "https://wiki.dynastynova.com/en/universe/coordinates"
title: "Coordinates"
description: "Galaxy, system, position and distances."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:23.069Z"
updated: "2026-10-05T19:40:28.716Z"
---

# Coordinates

> **In short**: every planet has a three-number address, [galaxy:system:position], for example [2:83:6]. The number of galaxies, of systems per galaxy and of positions per system depends on the universe (9 galaxies of 99 systems on Redline). The distance between two coordinates sets a flight's duration and hydrogen cost.
{.is-info}

> **Universe setting**: the number of galaxies, of systems per galaxy and of positions per system (9 to 20) depends on the universe.
> Redline: **9 galaxies**, **99 systems** per galaxy, **15 positions** per system
{.is-info}

## Rules

1. A coordinate reads **[galaxy:system:position]**.
2. Each galaxy has a fixed number of **systems**, which depends on the universe: **99** on Redline, numbered 1 to 99.
3. Each system has a fixed number of **positions** (15 on Redline). Each position holds at most one planet, plus possibly its moon.
4. Beyond the last position lies **deep space**, reserved for expeditions.
5. **The map is not circular**: galaxy 9 is not next to galaxy 1, and the last system is not next to the first.
6. The **distance** between two points depends on what separates them (table below).

## Summarized data

| Trip | Distance |
|---|---|
| To another galaxy | 20,000 × galaxy gap |
| Same galaxy, other system | 2,700 + 95 × system gap |
| Same system | 1,000 + 5 × position gap |
| Between a planet and its moon | 5 |

Deep space counts as the position after the last one: on Redline, position 16.

## Calculation

**Travel from Galaxy G1 to Galaxy G2** 

The distance from any planet in one galaxy to a planet in a different galaxy is: 

$$ D = 20\,000 \times |G_1 - G_2| $$

**Travel from System S1 to System S2**

The distance from any planet in one system to any planet in a different system is: 
$$ D = 2\,700 + 95 \times |S_1 - S_2| $$

**Travel from Planet P1 to Planet P2**

The distance between two planets in the same system is: 
$$ D = 1\,000 + 5 \times |P_1 - P_2| $$

## Worked examples

- to travel from any planet in galaxy 3 to a planet in galaxy 5 is:
$$ D = 20\,000 \times |3 - 5| = 40\,000 $$
- to travel from any planet in system 45 to a planet in system 50 is:
  $$ D = 2\,700 + 95 \times |45 - 50| = 3\,175 $$
- to travel from planet 3 to planet 6 in the same system is:
  $$ D = 1\,000 + 5 \times |3 - 6| = 1\,015 $$

## Common pitfalls

- **Crossing galaxies is expensive**: a single galaxy gap is already worth more than crossing a whole 99-system galaxy like Redline's (2,700 + 95 × 98 = 12,010).
- **No shortcut over the edge**: from galaxy 1 to galaxy 9, the gap is 8 galaxies.
- **Planet and moon are not in the same spot**: a distance of 5 is still a real, very short flight.

## Related pages

- [The galaxy view](/en/universe/galaxy-view)
- [Fleet movement](/en/fleet/movement)
- [Planets: size, temperature, type](/en/universe/planets)
- [Expeditions](/en/fleet/expeditions)
