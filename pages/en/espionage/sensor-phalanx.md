---
wiki_id: 124
locale: "en"
path: "espionage/sensor-phalanx"
url: "https://wiki.dynastynova.com/en/espionage/sensor-phalanx"
title: "Sensor phalanx"
description: "Watching fleets from a moon."
tags: ["espionage", "moon"]
published: true
created: "2026-10-02T13:11:48.294Z"
updated: "2026-10-02T17:40:26.409Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Sensor phalanx

> **In short**: the Sensor phalanx is built on a moon. It scans a planet in the same galaxy and reveals every fleet leaving from or heading to it: composition, mission and arrival time. Each scan costs 5,000 hydrogen.
{.is-info}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Sensor phalanx">

## Rules

1. The Sensor phalanx can be built **on a moon only**.
2. It can only scan a **planet** in the **same galaxy**, within range. It can **never target a moon**.
3. **Range** = level² − 1 systems on each side of the moon (minimum 1).
4. Each scan costs **5,000 hydrogen**, taken from the moon, even if no fleet is found.
5. The scan shows every fleet whose **origin or destination** is the planet, outbound and returning: **composition, mission and arrival time**. Enemy fleets included.
6. Fleet **cargo** stays hidden.
7. The scanned player is **never notified**.
8. A refused scan (out of range, other galaxy, invalid target) costs nothing.

## Worked example

Your moon is at [3:50:8] with a level 4 Sensor phalanx.
- Range: 4² − 1 = **15 systems** on each side, so systems 35 to 65 of galaxy 3.
- You can scan a planet at [3:60:5] for 5,000 hydrogen.
- A planet at [3:70:5] is out of range. A planet at [4:50:5] is in another galaxy: impossible.
- Near the edge, range is cut short: from [3:5:8], the same phalanx covers systems 1 to 20, because the map is not circular.

## Detailed data

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| Range (systems on each side) | 1 | 3 | 8 | 15 | 24 | 35 | 48 | 63 | 80 |

## Common pitfalls

- **A fleet stationed on a moon is invisible**: moons cannot be scanned. It is the best hiding place for a fleet.
- **Empty scans are paid too**: 5,000 hydrogen every time.
- **Keep hydrogen on the moon**: the cost is taken from the moon, not the planet.

## Related pages

- [Moons](/en/universe/moons)
- [Jump gate](/en/fleet/jump-gate)
- [Spying](/en/espionage/spying)
- [Coordinates](/en/universe/coordinates)
