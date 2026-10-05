---
wiki_id: 100
locale: "en"
path: "research/stellar-collaboration"
url: "https://wiki.dynastynova.com/en/research/stellar-collaboration"
title: "Stellar Collaboration"
description: "Networking your Innovation Centers."
tags: ["research"]
published: true
created: "2026-10-02T13:10:59.894Z"
updated: "2026-10-02T17:40:56.528Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Stellar Collaboration

> **In short**: Stellar Collaboration networks the Innovation Centers of your other planets to speed up your research. At level N, it adds the N best Centers of your other bases, provided they are at least as advanced as the Center of the planet starting the research.
{.is-info}

<img src="/images/illustrations/research/collaboration-stellaire.jpg" width="180" alt="Stellar Collaboration">

## Rules

1. Requirements: **Innovation Center 10, Quantum Computing 8, Hyperspace Technology 8**. Maximum level: 10.
2. At **level N**, research networks the **N best Innovation Centers** of your **other** planets.
3. A Center is only included if its level is **at least equal** to the Center of the planet starting the research.
4. **Effective level** = the planet's Center + the sum of networked Centers.
5. **Duration** of a research (in hours) = (metal + crystal) / (1,000 × (1 + effective level)), divided by the universe's research speed.
6. Stellar Collaboration **does not change research costs**.

## Worked example

You start a research from a planet whose Innovation Center is level **8**. Your other planets have Centers at levels 10, 9 and 6. Stellar Collaboration level **2**.
- Centers included: the 2 best among those at level 8 or more, so **10 and 9**. The level 6 Center is too weak.
- Effective level: 8 + 10 + 9 = **27**.
- Speed: (1 + 27) / (1 + 8) ≈ **3.1 times** faster than with the local Center alone.

## Common pitfalls

- **Start from the right Center**: a high local Center excludes weaker ones; a low local Center lowers the base. Compare before starting.
- **You need several equipped planets**: without another Innovation Center of sufficient level, Collaboration does nothing.

## Related pages

- [Technologies list](/en/research/technologies)
- [Tech tree](/en/research/tech-tree)
- [Colonization](/en/universe/colonization)
