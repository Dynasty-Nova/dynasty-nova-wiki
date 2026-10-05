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
updated: "2026-10-02T16:37:35.771Z"
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

## Worked example

From your planet at [2:40:8]:
- to [2:40:3], same system: 1,000 + 5 × 5 = **1,025**.
- to [2:45:3], same galaxy: 2,700 + 95 × 5 = **3,175**.
- to [5:10:1], other galaxy: 20,000 × 3 = **60,000**.
- to your moon at [2:40:8]: **5**.

## Detailed data

| Trip | Distance |
|---|---|
| To another galaxy | 20,000 × galaxy gap |
| Same galaxy, other system | 2,700 + 95 × system gap |
| Same system | 1,000 + 5 × position gap |
| Between a planet and its moon | 5 |

Deep space counts as the position after the last one: on Redline, position 16.

## Common pitfalls

- **Crossing galaxies is expensive**: a single galaxy gap is already worth more than crossing a whole 99-system galaxy like Redline's (2,700 + 95 × 98 = 12,010).
- **No shortcut over the edge**: from galaxy 1 to galaxy 9, the gap is 8 galaxies.
- **Planet and moon are not in the same spot**: a distance of 5 is still a real, very short flight.

## Related pages

- [The galaxy view](/en/universe/galaxy-view)
- [Fleet movement](/en/fleet/movement)
- [Planets: size, temperature, type](/en/universe/planets)
- [Expeditions](/en/fleet/expeditions)
