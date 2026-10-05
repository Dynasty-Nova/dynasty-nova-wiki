---
wiki_id: 112
locale: "en"
path: "defense/missiles"
url: "https://wiki.dynastynova.com/en/defense/missiles"
title: "Missiles"
description: "Ballistic Arsenal, Interception Missiles and Long-Range Warheads."
tags: ["defense", "missiles"]
published: true
created: "2026-10-02T13:11:23.628Z"
updated: "2026-10-02T17:40:29.534Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Missiles

> **In short**: missiles are stored in the Ballistic Arsenal. **Long-Range Warheads** destroy an enemy planet's defenses without sending a fleet. **Interception Missiles** shoot down Warheads aimed at your planet. Missiles never take part in fleet battles.
{.is-info}

> **Universe setting**: the attack limit, which also counts missile salvos, may differ from one universe to another.
> Default: **6 attacks per 24 h** · Redline: **6 attacks per 24 h**
{.is-info}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Ballistic Arsenal"> <img src="/images/illustrations/defense/intercepteurs.jpg" width="180" alt="Interception Missile"> <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="180" alt="Long-Range Warheads">

## Rules

### The Ballistic Arsenal
1. Missiles are stored in the **Ballistic Arsenal**, which offers **10 slots per level**.
2. An **Interception Missile** takes **1 slot**, a **Long-Range Warhead** takes **2**.
3. Missiles in the queue or under construction already count against the slots.
4. Missiles take no planet fields. Only the Arsenal itself takes one field per level.
5. Demolishing an Arsenal level while it is full destroys no missile.

### The missiles
6. Missiles **never fire during a battle** and do not count towards the planet's defensive power.
7. A Warhead salvo **only destroys defenses**: never buildings, the fleet in orbit or resources.
8. Defenses destroyed by a Warhead are **lost for good**: they do not get the free 70% repair.
9. **Target order**: without a designated target, Warheads hit the toughest defense first (shield + hull). If you designate a target, it is hit first, then the rest by decreasing toughness. If the planet has none of the designated defense, the normal order applies.
10. A salvo **cannot be recalled**. Warheads never come back, even if the target planet is abandoned in the meantime.

### Restrictions
11. A salvo **counts as one attack** towards the attack limit on the targeted player, across all their planets. Since it cannot be recalled, the slot is spent for good.
12. **Beginner protection** applies: a protected player cannot be targeted.
13. Firing a salvo **ends your own new player protection**, for good.
14. A player **on vacation** cannot be targeted, and you cannot fire while on vacation yourself.
15. During **maintenance**, missile strikes are suspended.

## Worked example

**Filling a level 3 Ballistic Arsenal**
- Capacity: 3 × 10 = **30 slots**.
- 10 Interception Missiles (10 slots) + 10 Long-Range Warheads (20 slots) = 30: the Arsenal is full.
- Cost of the 10 Warheads: 125,000 metal, 25,000 crystal, 100,000 hydrogen. Once fired, they are removed from your military points (250 points).

**A salvo with no designated target** against a planet defended by 1 Protective Dome, 5 Ion Batteries and 20 Ballistic Projectors
- The Protective Dome is the toughest defense: it is hit first, then the Ion Batteries, then the Projectors.
- Everything destroyed is lost, with no repair.

## Detailed data

### Missiles

| Missile | Metal | Crystal | Hydrogen | Points | Slots | Structure | Attack | Requirements |
|---|---|---|---|---|---|---|---|---|
| Interception Missile (game: Interceptors) | 8,000 | 2,000 | 0 | 10 | 1 | 8,000 | 1 | Orbital Dock 1, Ballistic Arsenal 2 |
| Long-Range Warheads | 12,500 | 2,500 | 10,000 | 25 | 2 | 15,000 | 12,000 | Orbital Dock 1, Ballistic Arsenal 4, Impulse Drive 1 |

Missiles count as military points.

### Ballistic Arsenal

Requirement: Orbital Dock 1. Maximum level: 10. The cost doubles at each level.

| Level | Metal | Crystal | Hydrogen | Slots |
|---|---|---|---|---|
| 1 | 20,000 | 20,000 | 1,000 | 10 |
| 2 | 40,000 | 40,000 | 2,000 | 20 |
| 3 | 80,000 | 80,000 | 4,000 | 30 |
| 4 | 160,000 | 160,000 | 8,000 | 40 |
| 5 | 320,000 | 320,000 | 16,000 | 50 |
| 6 | 640,000 | 640,000 | 32,000 | 60 |
| 7 | 1,280,000 | 1,280,000 | 64,000 | 70 |
| 8 | 2,560,000 | 2,560,000 | 128,000 | 80 |
| 9 | 5,120,000 | 5,120,000 | 256,000 | 90 |
| 10 | 10,240,000 | 10,240,000 | 512,000 | 100 |

## Common pitfalls

- **Interception Missile is not the Interceptor**: the missile and the combat ship have nothing in common.
- **The Dome goes first**: without a designated target, the toughest defense is hit first. Designate a target if you are after something else.
- **A salvo costs an attack slot**: it counts towards the attack limit on that player, even if it destroys nothing.
- **End of new player protection**: your first salvo ends it, just like a fleet attack.
- **Missiles do not defend against fleets**: only Interception Missiles serve in defense, and only against Warheads.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Attack limit](/en/players/attack-limit)
- [Beginner protection](/en/players/beginner-protection)
- [Defense rebuild](/en/combat/defense-rebuild)
- [Maintenance](/en/misc/maintenance)
