---
wiki_id: 114
locale: "en"
path: "combat/how-combat-works"
url: "https://wiki.dynastynova.com/en/combat/how-combat-works"
title: "How combat works"
description: "Rounds, shots, shields, explosions and outcome."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:27.663Z"
updated: "2026-10-02T16:38:19.380Z"
---

# How combat works

> **In short**: a battle lasts at most 6 rounds. Each round, shields recharge, the attacker fires, then the defender. Each shot targets a random enemy unit and always hits. A shot that is too weak bounces off shields; a shot that damages the hull may make its target explode.
{.is-info}

## Rules

### Combat stats
1. **Attack** = base attack × (1 + 0.1 × Weapon Systems).
2. **Shield** = base shield × (1 + 0.1 × Shielding Technology).
3. **Hull** = structure × (1 + 0.1 × Armor Technology) / 10.
4. The Weapons doctrine and Protection doctrine alliance talents add 5%.

### How a round unfolds
5. A battle has **at most 6 rounds**. It stops as soon as one side has no units left.
6. At the start of each round, **all shields recharge** fully and unit counts are frozen.
7. **The attacker fires, then the defender.** A unit alive at the start of the round fires all its shots, even if it is destroyed during the round: in practice, fire is simultaneous.
8. Each shot targets an **enemy unit picked at random** among living units. **Every shot hits.**
9. After a shot, a ship with [rapid fire](/en/fleet/rapid-fire) against its target may fire again.

### Damage
10. **1% rule**: a shot below 1% of the target's maximum shield **bounces** with no effect.
11. Otherwise, the **shield absorbs** damage as long as it lasts, and the rest goes entirely to the **hull**.
12. **Explosion**: after a shot that damages the hull without destroying it, if the hull drops below 70%, the unit explodes with a probability of **1 − share of hull left**. A bounced shot does not trigger this roll.

### Outcome
13. **Attacker wins** if the defender has no units left; **defender wins** if the attacker has no units left; otherwise it is a **draw** (both sides still standing after 6 rounds, or both wiped out).
14. Plunder only happens when the attacker wins.
15. Every battle is **deterministic**: replayed, it gives exactly the same result.

## Worked example

**A Battleship (attack 1,000) fires at an Interceptor** (shield 10, hull 400, no research)
- The shield absorbs 10, the hull takes 990: the Interceptor is **destroyed**.

**4 Interceptors (attack 50) fire at a Battleship** (shield 200, hull 6,000)
- 1% threshold: 2. The shots go through.
- The 4 shots (200 in total) empty the shield, **without touching the hull**. Next round, the shield is full again.

**A unit whose hull drops to 60%**
- Chance of exploding: 1 − 0.60 = **40%**.

## Common pitfalls

- **Small shots crash on shields**: a handful of weak units may never dent a big target's hull, since shields recharge every round.
- **Targets are random**: you do not choose what your ships aim at. Numerous cheap units soak up many shots.
- **6 rounds, no more**: if nobody is wiped out, it is a draw and the attacker plunders nothing.
- **Defenses fire too**: each defense fires once per round, with no rapid fire.

## Related pages

- [Rapid fire](/en/fleet/rapid-fire)
- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [Plunder](/en/combat/plunder)
- [Reading a battle report](/en/combat/battle-report)
- [Battle simulator](/en/combat/simulator)
