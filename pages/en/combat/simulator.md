---
wiki_id: 119
locale: "en"
path: "combat/simulator"
url: "https://wiki.dynastynova.com/en/combat/simulator"
title: "Battle simulator"
description: "Planning an attack with the simulator."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:38.050Z"
updated: "2026-10-02T16:38:26.529Z"
---

# Battle simulator

> **In short**: the simulator estimates a battle's outcome before you commit. You can import a spy report or enter forces by hand. It computes a win chance and an estimate of the debris field.
{.is-info}

## Rules

1. The simulator can **import a spy report**: the recorded values are filled in automatically.
2. A category the report did **not reach** (for example the fleet) is assumed **empty**: the win chance shown is then an **optimistic floor**. Enter an estimate if you have one.
3. If the report did not reach the target's **research**, its technologies are assumed **equal to yours**.
4. Editing an imported value switches the simulation to **manual input**: the report is no longer used.
5. The simulator also estimates the **debris field** of an average battle, at your universe's debris rate.
6. Simulations that are too large are refused: the server caps units per side and the number of runs.

## Worked example

You import a report with effective level 3: resources and fleet known, but neither defenses nor research. The simulator assumes zero defenses and technologies equal to yours. If the target actually has 20 Ion Batteries, your real win chance will be **lower** than shown.

## Common pitfalls

- **An incomplete report makes the simulator optimistic**: fill in missing categories before trusting the result.
- **Technologies matter**: if you know the target's, enter them.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [How combat works](/en/combat/how-combat-works)
- [Debris fields](/en/combat/debris)
