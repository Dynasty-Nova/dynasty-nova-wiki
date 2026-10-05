---
wiki_id: 127
locale: "en"
path: "players/beginner-protection"
url: "https://wiki.dynastynova.com/en/players/beginner-protection"
title: "Beginner protection"
description: "Who can attack whom: new player protection and point tiers."
tags: ["players"]
published: true
created: "2026-10-02T13:11:54.297Z"
updated: "2026-10-02T16:38:37.801Z"
---

# Beginner protection

> **In short**: two protections keep mismatched players from fighting. **New player protection** makes you unattackable for your first 7 days. **Points-based protection** forbids any attack between two players whose points are too far apart, in either direction.
{.is-info}

> **Universe setting**: point tiers, new player protection length and the inactivity delay may differ from one universe to another.
> Default and Redline: tiers **1:3 / 1:5 / 1:10**, new player protection **7 days**, inactivity **14 days**
{.is-info}

## Rules

### New player protection
1. For **7 days** after you first join a universe, nobody can attack you. The remaining time shows at the top of the screen, and your planets carry a "New player" badge.
2. **Launching an attack or a missile salvo ends it, for good.** A warning appears before you confirm.
3. Spying, transport and other missions do not remove it.

### Points-based protection
4. You cannot attack a player **much weaker or much stronger** than you. The allowed gap depends on the tier of the **weaker** of the two players.
5. Tiers, by the weaker player's points:
   - under 500 points: maximum gap **1:3**;
   - from 500 to under 5,000 points: **1:5**;
   - from 5,000 to under 500,000 points: **1:10**;
   - 500,000 points or more: **no protection at all**.
6. A boundary belongs to the upper tier: a player with exactly 5,000 points is at 1:10.
7. A protected player can still be **spied on**.
8. **Missile salvos** follow the same rules as an attack.
9. A player **inactive for 14 days** loses protection: anyone can attack them, whatever the points gap.
10. Both protections stack.

## Worked example

| Player A | Player B | Weaker player's tier | Gap | Attack possible? |
|---|---|---|---|---|
| 400 points | 1,000 points | 1:3 (A < 500) | 2.5 | yes, both ways |
| 400 points | 1,500 points | 1:3 (A < 500) | 3.75 | **no, neither A nor B** |
| 6,000 points | 50,000 points | 1:10 (A ≥ 5,000) | 8.3 | yes, both ways |
| 6,000 points | 80,000 points | 1:10 | 13.3 | **no, neither A nor B** |
| 600,000 points | 5,000,000 points | none (A ≥ 500,000) | | yes |

## Common pitfalls

- **The stronger player is protected too**: a small player cannot attack a much bigger one.
- **Your first attack costs you your 7 days**: think twice before attacking during your first week.
- **Inactivity lifts everything**: after 14 days without logging in, anyone can attack you. Consider [vacation mode](/en/players/vacation-mode) before a long absence.
- **Points count everything**: economy, research and military. Building a lot can move you to another tier.

## Related pages

- [Rankings and points](/en/players/rankings)
- [Attack limit](/en/players/attack-limit)
- [Vacation mode](/en/players/vacation-mode)
- [Inactivity](/en/players/inactivity)
- [The galaxy view](/en/universe/galaxy-view)
