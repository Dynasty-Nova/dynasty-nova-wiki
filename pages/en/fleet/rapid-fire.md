---
wiki_id: 103
locale: "en"
path: "fleet/rapid-fire"
url: "https://wiki.dynastynova.com/en/fleet/rapid-fire"
title: "Rapid fire"
description: "Which units fire several times at which targets."
tags: ["fleet", "combat"]
published: true
created: "2026-10-02T13:11:06.074Z"
updated: "2026-10-02T16:38:05.031Z"
---

# Rapid fire

> **In short**: some ships have **rapid fire** against certain targets. After shooting one of them, they have a chance to fire again in the same round. The listed factor is the average number of shots a ship chains against that kind of target. Defenses never have rapid fire.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. Each round, every unit fires at least once at an enemy target picked at random among living units.
2. After each shot, if the shooter has rapid fire of factor **f** against the target it just hit, it fires again with a probability of **1 − 1/f**, at a **new random target**.
3. It keeps going as long as the roll succeeds **and** the new target is also covered by rapid fire. If the new target is not, the chain stops after that shot.
4. Against a fleet made only of that target, the shooter fires **f times on average** per round.

## Worked example

The Corvette has rapid fire **6** against the Interceptor.
- After shooting an Interceptor, it fires again with a probability of 1 − 1/6 = **83.3%**.
- Against a fleet of Interceptors only, it fires **6 times on average** per round instead of once.
- Against a mixed fleet (half Interceptors, half Battleships), the chain stops as soon as it lands on a Battleship: it fires noticeably less.

## Detailed data

### Who rapid-fires at whom

| Shooter | Targets (factor) |
|---|---|
| Cargo Shuttle | Scout 5, Solar Collector 5 |
| Stellar Freighter | Scout 5, Solar Collector 5 |
| Space Pioneer | Scout 5, Solar Collector 5 |
| Salvager | Scout 5, Solar Collector 5 |
| Interceptor | Scout 5, Solar Collector 5 |
| Assailant | Scout 5, Solar Collector 5, Cargo Shuttle 3 |
| Corvette | Ballistic Projector 10, Interceptor 6, Scout 5, Solar Collector 5 |
| Battleship | Scout 5, Solar Collector 5 |
| Orbital Striker | Ballistic Projector 20, Photonic Cannon 20, High-Energy Emitter 10, Ion Battery 10, Magnetic Accelerator 5, Plasma Ejector 5, Scout 5, Solar Collector 5 |
| Predator | Battleship 7, Corvette 4, Assailant 4, Cargo Shuttle 3, Stellar Freighter 3, Scout 5, Solar Collector 5 |
| Annihilator | Photonic Cannon 10, Predator 2, Scout 5, Solar Collector 5 |
| Stellar Colossus | Scout 1,250, Solar Collector 1,250, Space Pioneer 250, Stellar Freighter 250, Salvager 250, Cargo Shuttle 250, Ballistic Projector 200, Interceptor 200, Photonic Cannon 200, Assailant 100, High-Energy Emitter 100, Ion Battery 100, Magnetic Accelerator 50, Corvette 33, Battleship 30, Orbital Striker 25, Predator 15, Annihilator 5 |
| Scout, Solar Collector | none |
| All defenses | none |

### Who is targeted by what

| Target | Ships with rapid fire against it |
|---|---|
| Scout, Solar Collector | Every ship except the Scout and the Solar Collector |
| Cargo Shuttle | Assailant 3, Predator 3, Colossus 250 |
| Stellar Freighter | Predator 3, Colossus 250 |
| Interceptor | Corvette 6, Colossus 200 |
| Assailant | Predator 4, Colossus 100 |
| Corvette | Predator 4, Colossus 33 |
| Battleship | Predator 7, Colossus 30 |
| Predator | Annihilator 2, Colossus 15 |
| Orbital Striker | Colossus 25 |
| Annihilator | Colossus 5 |
| Stellar Colossus | nobody |
| Ballistic Projector | Orbital Striker 20, Corvette 10, Colossus 200 |
| Photonic Cannon | Orbital Striker 20, Annihilator 10, Colossus 200 |
| High-Energy Emitter, Ion Battery | Orbital Striker 10, Colossus 100 |
| Magnetic Accelerator | Orbital Striker 5, Colossus 50 |
| Plasma Ejector | Orbital Striker 5 |
| Defensive Barrier, Protective Dome | nobody |

## Common pitfalls

- **Scouts and Solar Collectors feed enemy chains**: almost every ship has rapid fire 5 against them. Leaving many Scouts or Collectors in orbit during an attack hands the attacker extra shots.
- **Rapid fire guarantees nothing**: the next target is random. In a mixed fleet, chains are shorter than the listed factor.
- **No ship has rapid fire against the Stellar Colossus**: it can only be brought down by regular shots.
- **Rapid fire does not bypass the 1% rule**: a shot too weak for a big shield bounces, even inside a chain.

## Related pages

- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [How combat works](/en/combat/how-combat-works)
- [Battle simulator](/en/combat/simulator)
