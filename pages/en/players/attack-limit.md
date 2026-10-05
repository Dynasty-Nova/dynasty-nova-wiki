---
wiki_id: 128
locale: "en"
path: "players/attack-limit"
url: "https://wiki.dynastynova.com/en/players/attack-limit"
title: "Attack limit"
description: "6 attacks per player per 24-hour window."
tags: ["players"]
published: true
created: "2026-10-02T13:11:56.425Z"
updated: "2026-10-02T16:38:39.212Z"
---

# Attack limit

> **In short**: you can attack the same player at most **6 times per 24-hour window**, all their planets together, missile salvos included. The window opens with your first attack on them. The 7th attack is refused at launch.
{.is-info}

> **Universe setting**: the number of attacks and the window length may differ from one universe to another (0 disables the rule).
> Default and Redline: **6 attacks per 24 h**
{.is-info}

## Rules

1. The limit applies to **one target player**, all their planets together.
2. What counts: **fleet attacks** and **missile salvos**. What does not: espionage, transport, recycling.
3. The **24-hour window is fixed**: it opens with your first attack on that player and resets 24 hours later.
4. The **7th attack** in the window is **refused at launch**.
5. **Recalling** a fleet before it arrives gives the slot back. A missile salvo cannot be recalled: its slot is spent.
6. **Abandoned planets** are not concerned.
7. Alliance wars and pacts do not change the limit.
8. The galaxy view shows how many attacks you have left against each player.

## Worked example

| Time | Action against player X | Attacks remaining |
|---|---|---|
| Monday 10:00 | 1st attack: the window opens until Tuesday 10:00 | 5 |
| Monday 12:00 | 2nd attack | 4 |
| Monday 14:00 | Missile salvo | 3 |
| Monday 15:00 | 3rd fleet attack, recalled before arrival | 3 (slot given back) |
| Monday 18:00 to 22:00 | 3 attacks | 0 |
| Monday 23:00 | New attack: **refused** | 0 |
| Tuesday 10:00 | The window resets | 6 |

## Common pitfalls

- **The window does not slide**: it starts from your first attack, not your last.
- **Missiles count**: a salvo is a full attack, and it cannot be recalled.
- **All their planets count together**: attacking two different colonies of the same player uses two slots.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Missiles](/en/defense/missiles)
- [The galaxy view](/en/universe/galaxy-view)
- [Plunder](/en/combat/plunder)
