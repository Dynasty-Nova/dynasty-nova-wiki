---
wiki_id: 110
locale: "en"
path: "defense/defenses"
url: "https://wiki.dynastynova.com/en/defense/defenses"
title: "Defenses list"
description: "Defenses: costs, stats, requirements."
tags: ["defense"]
published: true
created: "2026-10-02T13:11:19.721Z"
updated: "2026-10-02T17:40:07.729Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Defenses list

> **In short**: defenses protect your planet around the clock. They never move, cannot be plundered and, after a battle, each destroyed defense has a 70% chance of being repaired for free. This page covers the 8 defenses. Missiles have their own page: [Missiles](/en/defense/missiles).
{.is-info}

> **Universe setting**: the share of destroyed defenses that turns into a debris field may differ from one universe to another.
> Default: **0%** · Redline: **0%**
{.is-info}

## Rules

1. Defenses are built at the **Orbital Dock**. They are **paid per unit when queued**.
2. They take part in every battle fought on their planet, against any attacking fleet.
3. **Free repair**: after a battle, each destroyed defense gets its own roll. It has a **70% chance** of being repaired at no cost and a 30% chance of being lost.
4. **Defensive Barrier and Protective Dome**: one of each per planet. You cannot order or queue a second one while the first exists. In combat they are ordinary targets with a very large shield: they **do not protect other units**.
5. Destroyed defenses leave **no debris field** (unless the universe says otherwise).
6. Defenses destroyed by a **missile** are never repaired.
7. Defenses have **no rapid fire**. Some ships, however, have rapid fire against them (see [Rapid fire](/en/fleet/rapid-fire)).
8. In combat, attack, shield and structure rise by 10% per level of Weapon Systems, Shielding Technology and Armor Technology. The combat **hull** equals structure divided by 10.
9. **Points**: each defense is worth 1 point per 1,000 resources of its cost, counted as military points.

## Worked example

**10 Ballistic Projectors destroyed in an attack**
- Each has a 70% chance of being repaired: **7** come back on average, but the result can be anything from 0 to 10.
- Chance that all 10 come back: 0.7^10, about **2.8%**.

**Your Protective Dome is destroyed**
- 70% chance it is repaired, **30% chance of losing it** for good. You can then build a new one.

**A weak shot bounces**
- A shot below 1% of the target's shield has no effect.
- A Ballistic Projector (attack 80) damages a Battleship (shield 200, threshold 2), but not a Stellar Colossus (shield 50,000, threshold 500).

## Detailed data

### Costs and base stats (no research)

| Defense | Metal | Crystal | Hydrogen | Points | Structure | Combat hull | Shield | Attack |
|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/projecteur-balistique.jpg" width="48" alt="Ballistic Projector"> Ballistic Projector | 2,000 | 0 | 0 | 2 | 2,000 | 200 | 20 | 80 |
| <img src="/images/illustrations/defense/canon-photonique.jpg" width="48" alt="Photonic Cannon"> Photonic Cannon | 1,500 | 500 | 0 | 2 | 2,000 | 200 | 25 | 100 |
| <img src="/images/illustrations/defense/emetteur-a-haute-energie.jpg" width="48" alt="High-Energy Emitter"> High-Energy Emitter | 6,000 | 2,000 | 0 | 8 | 8,000 | 800 | 100 | 250 |
| <img src="/images/illustrations/defense/batterie-ionique.jpg" width="48" alt="Ion Battery"> Ion Battery | 2,000 | 6,000 | 0 | 8 | 8,000 | 800 | 500 | 150 |
| <img src="/images/illustrations/defense/accelerateur-magnetique.jpg" width="48" alt="Magnetic Accelerator"> Magnetic Accelerator | 20,000 | 15,000 | 2,000 | 37 | 35,000 | 3,500 | 200 | 1,100 |
| <img src="/images/illustrations/defense/ejecteur-a-plasma.jpg" width="48" alt="Plasma Ejector"> Plasma Ejector | 50,000 | 50,000 | 30,000 | 130 | 100,000 | 10,000 | 300 | 3,000 |
| <img src="/images/illustrations/defense/barriere-defensive.jpg" width="48" alt="Defensive Barrier"> Defensive Barrier | 10,000 | 10,000 | 0 | 20 | 20,000 | 2,000 | 2,000 | 1 |
| <img src="/images/illustrations/defense/dome-protecteur.jpg" width="48" alt="Protective Dome"> Protective Dome | 50,000 | 50,000 | 0 | 100 | 100,000 | 10,000 | 10,000 | 1 |

Each defense fires once per round.

### Requirements

| Defense | Orbital Dock | Research | Copies |
|---|---|---|---|
| Ballistic Projector | 1 | none | unlimited |
| Photonic Cannon | 2 | Laser Technology 3 | unlimited |
| High-Energy Emitter | 4 | Laser Technology 6, Energy Science 3 | unlimited |
| Ion Battery | 4 | Ion Technology 4 | unlimited |
| Magnetic Accelerator | 6 | Weapon Systems 3, Shielding Technology 1, Energy Science 6 | unlimited |
| Plasma Ejector | 8 | Plasma Technology 7 | unlimited |
| Defensive Barrier | 1 | Shielding Technology 2 | 1 |
| Protective Dome | 6 | Shielding Technology 6 | 1 |

### Ships with rapid fire against defenses

Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).

| Defense | Rapid fire taken |
|---|---|
| Ballistic Projector | Orbital Striker 20, Corvette 10, Stellar Colossus 200 |
| Photonic Cannon | Orbital Striker 20, Annihilator 10, Stellar Colossus 200 |
| High-Energy Emitter | Orbital Striker 10, Stellar Colossus 100 |
| Ion Battery | Orbital Striker 10, Stellar Colossus 100 |
| Magnetic Accelerator | Orbital Striker 5, Stellar Colossus 50 |
| Plasma Ejector | Orbital Striker 5 |
| Defensive Barrier, Protective Dome | none |

## Common pitfalls

- **Repair is not guaranteed**: 70% is a chance per unit, not a share of the batch. With few defenses, you can lose them all.
- **Planetary shields do not cover the planet**: the Barrier and the Dome absorb shots for themselves only, they do not reduce damage to other units.
- **The Orbital Striker hunts defenses**: it has rapid fire against almost all of them. Against it, rely on the defenses it hits least (Plasma Ejector, shields).
- **Defenses give the attacker nothing back**: by default they leave no debris field. A heavily defended planet is costly to attack and yields no wreckage.
- **Missiles**: a defense destroyed by a Long-Range Warhead is lost for good.

## Related pages

- [Missiles](/en/defense/missiles)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Rapid fire](/en/fleet/rapid-fire)
- [Defense rebuild](/en/combat/defense-rebuild)
- [How combat works](/en/combat/how-combat-works)
- [Ships list](/en/fleet/ships)
