---
wiki_id: 82
locale: "en"
path: "universe/galaxy-view"
url: "https://wiki.dynastynova.com/en/universe/galaxy-view"
title: "The galaxy view"
description: "Reading the galaxy view, system by system."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:25.037Z"
updated: "2026-10-02T17:41:09.034Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# The galaxy view

> **In short**: the galaxy view shows one system at a time, position by position. For each planet you see its owner, its status, its debris, its moon and how many attacks you have left against that player. From here you can also spy in one click, share a position with your alliance or bookmark it.
{.is-info}

![The galaxy view, orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*The galaxy view in orbit layout: each planet has its own look, set by its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

![The galaxy view, list layout](/images/screenshots/english/galaxy-view.jpg)
*In list layout, positions not yet spied on stay unreadable. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

1. The galaxy view shows **one system**: all its positions, then deep space.
2. **Navigation**: ← / → keys to change system, Ctrl + ← / → (⌘ on Mac) to change galaxy.
3. Two layouts are available: **list** or **orbits**.
4. **Hidden positions**: until a position has been spied on, everything there stays hidden. An exotic, unreadable script replaces the planet's name and its owner's. An unreadable cell may be free or occupied: only espionage tells.
5. A **spied** position reveals the planet, its owner, their points and their **statuses**. With Espionage Technology 10, a spied cell stays discovered for good.
6. The **"Attacks remaining: x / 6"** counter tells you how many attacks you have left against that player in the current 24-hour window.
7. The **quick spy** button sends a Scout in one click from your current planet. You need a Scout available on that planet.
8. A cell's sheet also shows the planet's **size**, its **used fields** and its **temperature**.
9. You can **share a position** with your alliance: each member opens it in their own galaxy view. The message stays 30 days in the channel.
10. A **star** adds the position to your **bookmarks**, with an optional private note.

## Worked example

You have already attacked a player twice today. On their row, the counter shows **"Attacks remaining: 4 / 6"**. After four more attacks it will show 0 / 6, and any new attack will be refused until the 24-hour window ends.

## Detailed data

### Statuses shown

| Status | Meaning |
|---|---|
| Protected beginner | Player protected by the points gap with you (see [Beginner protection](/en/players/beginner-protection)) |
| New player | Player in their first 7 days, cannot be attacked |
| On vacation | Player in vacation mode: no attack, transport or missiles |
| Abandoned | Abandoned planet, decaying before it disappears |
| Uninhabited | Free position, can be colonized |
| Recently spied | You have a recent spy report on this planet |
| Debris field | Debris in orbit, to recycle |

## Common pitfalls

- **An unreadable cell tells nothing**: it may hide a player or be empty. Send a Scout before drawing conclusions.
- **The attack counter is per player**: it counts all their planets together, missile salvos included.
- **Quick spy leaves from the selected planet**: without a Scout on that planet, the button does nothing.
- **Debris belongs to everyone**: a debris field spotted in the galaxy goes to whoever recycles it first.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Beginner protection](/en/players/beginner-protection)
- [Attack limit](/en/players/attack-limit)
- [Spying](/en/espionage/spying)
- [Empire view and bookmarks](/en/misc/empire-and-bookmarks)
