"""Génère edits/2026-10-02-illustrations.json : textes (positions masquées, biomes, pas de pay to win, skins),
vignettes dans les tableaux et illustrations en tête de page."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'pages'
SEP = '\n---\n\n'
IMG = '/images/illustrations'
V_FR = 'Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.'
V_EN = 'Screenshot from game version Server 2.1.0 · Client 3.1.0.'


def body(key):
    return (ROOT / f'{key}.md').read_text(encoding='utf-8').split(SEP, 1)[1]


def thumb(path, alt, width=48):
    return f'<img src="{IMG}/{path}.jpg" width="{width}" alt="{alt}">'


def row_thumbs(key, rows):
    """rows: [(texte de la 1re cellule, chemin image)] ; ajoute une vignette dans la 1re ligne de tableau qui commence par cette cellule."""
    text = body(key)
    pairs = []
    for cell, path in rows:
        prefix = f'| {cell} |'
        line = next((l for l in text.split('\n') if l.startswith(prefix)), None)
        if line is None:
            raise SystemExit(f'ligne introuvable dans {key} : {cell}')
        alt = cell.replace('*', '')
        pairs.append([line, line.replace(prefix, f'| {thumb(path, alt)} {cell} |', 1)])
    return pairs


def header(key, images, heading):
    """Insère une rangée d'illustrations juste avant le titre de section donné (« ## Règles » ou « ## Rules »)."""
    tags = ' '.join(thumb(p, alt, 180) for p, alt in images)
    return [[f'\n{heading}\n', f'\n{tags}\n\n{heading}\n']]


E = {}

# --- Vaisseaux ---
ships = [('navette-de-fret', 'Navette de fret', '*Cargo Shuttle* (Navette de fret)'),
         ('cargo-stellaire', 'Cargo stellaire', '*Stellar Freighter* (Cargo stellaire)'),
         ('pionnier-spatial', 'Pionnier spatial', '*Space Pioneer* (Pionnier spatial)'),
         ('recuperateur', 'Récupérateur', '*Salvager* (Récupérateur)'),
         ('eclaireur', 'Éclaireur', '*Scout* (Éclaireur)'),
         ('collecteur-solaire', 'Collecteur solaire', '*Solar Collector* (Collecteur solaire)'),
         ('intercepteur', 'Intercepteur', '*Interceptor* (Intercepteur)'),
         ('assaillant', 'Assaillant', '*Assailant* (Assaillant)'),
         ('corvette', 'Corvette', '*Corvette* (Corvette)'),
         ('cuirasse', 'Cuirassé', '*Battleship* (Cuirassé)'),
         ('frappe-orbital', 'Frappe-orbital', '*Orbital Striker* (Frappe-orbital)'),
         ('predateur', 'Prédateur', '*Predator* (Prédateur)'),
         ('annihilateur', 'Annihilateur', '*Annihilator* (Annihilateur)'),
         ('colossus-stellaire', 'Colossus stellaire', 'Stellar Colossus (Colossus stellaire)')]
E['fr/fleet/ships'] = row_thumbs('fr/fleet/ships', [(fr, f'ships/{f}') for f, fr, en in ships])
E['en/fleet/ships'] = row_thumbs('en/fleet/ships', [(en, f'ships/{f}') for f, fr, en in ships])

# --- Défenses ---
defs = [('projecteur-balistique', 'Projecteur balistique', 'Ballistic Projector'),
        ('canon-photonique', 'Canon photonique', 'Photonic Cannon'),
        ('emetteur-a-haute-energie', 'Émetteur à haute énergie', 'High-Energy Emitter'),
        ('batterie-ionique', 'Batterie ionique', 'Ion Battery'),
        ('accelerateur-magnetique', 'Accélérateur magnétique', 'Magnetic Accelerator'),
        ('ejecteur-a-plasma', 'Éjecteur à plasma', 'Plasma Ejector'),
        ('barriere-defensive', 'Barrière défensive', 'Defensive Barrier'),
        ('dome-protecteur', 'Dôme protecteur', 'Protective Dome')]
E['fr/defense/defenses'] = row_thumbs('fr/defense/defenses', [(fr, f'defense/{f}') for f, fr, en in defs])
E['en/defense/defenses'] = row_thumbs('en/defense/defenses', [(en, f'defense/{f}') for f, fr, en in defs])

# --- Bâtiments ---
blds = [('buildings/base-planetaire', 'Base planetaire / Base Coloniale', 'Planetary Base / Colonial Base'),
        ('buildings/excavateur-mineral', 'Excavateur minéral', 'Mineral Excavator'),
        ('buildings/extracteur-cristallin', 'Extracteur cristallin', 'Crystal Extractor'),
        ('buildings/condensateur-d-hydrogene', "Condensateur d'hydrogène", 'Hydrogen Condenser'),
        ('buildings/capteurs-photovoltaiques', 'Capteurs photovoltaïques', 'Photovoltaic Sensors'),
        ('buildings/reacteur-thermonucleaire', 'Réacteur thermonucléaire', 'Thermonuclear Reactor'),
        ('buildings/depot-alliages', "Dépôt d'alliages", 'Alloy Depot'),
        ('buildings/chambre-cristalline', 'Chambre cristalline', 'Crystal Chamber'),
        ('buildings/citerne-hydrogene', "Citerne d'hydrogène", 'Hydrogen Tank'),
        ('facilities/centre-d-innovation', "Centre d'innovation", 'Innovation Center'),
        ('facilities/fabrique-d-automates', "Fabrique d'automates", 'Automaton Factory'),
        ('facilities/dock-orbital', 'Dock orbital', 'Orbital Dock'),
        ('facilities/assembleur-moleculaire', 'Assembleur moléculaire', 'Molecular Assembler'),
        ('facilities/station-de-reparation', 'Station de réparation', 'Repair Station'),
        ('facilities/modulateur-planetaire', 'Modulateur planétaire', 'Planetary Modulator'),
        ('facilities/arsenal-balistique', 'Arsenal balistique', 'Ballistic Arsenal'),
        ('facilities/centre-logistique', 'Centre logistique', 'Logistics Center'),
        ('facilities/base-lunaire', 'Base lunaire', 'Lunar base'),
        ('facilities/phalange-de-capteur', 'Phalange de capteur', 'Sensor phalanx'),
        ('facilities/porte-de-saut', 'Porte de saut', 'Jump gate')]
E['fr/economy/buildings'] = row_thumbs('fr/economy/buildings', [(fr, p) for p, fr, en in blds])
E['en/economy/buildings'] = row_thumbs('en/economy/buildings', [(en, p) for p, fr, en in blds])

# --- Technologies ---
techs = [('science-energetique', 'Science Énergétique', 'Energy Science'),
         ('maitrise-du-plasma', 'Maîtrise du Plasma', 'Plasma Technology'),
         ('calcul-quantique', 'Calcul Quantique', 'Quantum Computing'),
         ('collaboration-stellaire', 'Collaboration Stellaire', 'Stellar Collaboration'),
         ('diplomatie-stellaire', 'Diplomatie Stellaire', 'Stellar Diplomacy'),
         ('propulseur-chimique', 'Propulseur Chimique', 'Combustion Drive'),
         ('moteur-magnetique', 'Moteur Magnétique', 'Impulse Drive'),
         ('navigation-transdimensionnelle', 'Navigation Transdimensionnelle', 'Hyperspace Drive'),
         ('systemes-photoniques', 'Systèmes Photoniques', 'Laser Technology'),
         ('manipulation-ionique', 'Manipulation Ionique', 'Ion Technology'),
         ('pliage-spatial', 'Pliage Spatial', 'Hyperspace Technology'),
         ('systemes-offensifs', 'Systèmes Offensifs', 'Weapon Systems'),
         ('champs-de-protection', 'Champs de Protection', 'Shielding Technology'),
         ('metallurgie-avancee', 'Métallurgie Avancée', 'Armor Technology'),
         ('manipulation-gravitationnelle', 'Manipulation Gravitationnelle', 'Graviton Technology'),
         ('renseignement-tactique', 'Renseignement Tactique', 'Espionage Technology'),
         ('cosmologie-appliquee', 'Cosmologie Appliquée', 'Astrophysics')]
E['fr/research/technologies'] = row_thumbs('fr/research/technologies', [(fr, f'research/{f}') for f, fr, en in techs])
E['en/research/technologies'] = row_thumbs('en/research/technologies', [(en, f'research/{f}') for f, fr, en in techs])

# --- Illustrations en tête de page ---
heads = {
    'economy/repair-station': [('facilities/station-de-reparation', 'Station de réparation', 'Repair Station')],
    'economy/terraformer-and-logistics': [('facilities/modulateur-planetaire', 'Modulateur planétaire', 'Planetary Modulator'), ('facilities/centre-logistique', 'Centre logistique', 'Logistics Center')],
    'fleet/jump-gate': [('facilities/porte-de-saut', 'Porte de saut', 'Jump gate')],
    'espionage/sensor-phalanx': [('facilities/phalange-de-capteur', 'Phalange de capteur', 'Sensor phalanx')],
    'defense/missiles': [('facilities/arsenal-balistique', 'Arsenal balistique', 'Ballistic Arsenal'), ('defense/intercepteurs', 'Intercepteurs', 'Interception Missile'), ('defense/ogives-longue-portee', 'Ogives longue portée', 'Long-Range Warheads')],
    'defense/shield-domes': [('defense/barriere-defensive', 'Barrière défensive', 'Defensive Barrier'), ('defense/dome-protecteur', 'Dôme protecteur', 'Protective Dome')],
    'universe/colonization': [('ships/pionnier-spatial', 'Pionnier spatial', 'Space Pioneer')],
    'combat/debris': [('ships/recuperateur', 'Récupérateur', 'Salvager')],
    'espionage/spying': [('ships/eclaireur', 'Éclaireur', 'Scout')],
    'combat/moon-destruction': [('ships/colossus-stellaire', 'Colossus stellaire', 'Stellar Colossus')],
    'economy/resources': [('resources/metal', 'Métal', 'Metal'), ('resources/crystal', 'Cristal', 'Crystal'), ('resources/hydrogene', 'Hydrogène', 'Hydrogen'), ('resources/energy', 'Énergie', 'Energy')],
    'economy/energy': [('buildings/capteurs-photovoltaiques', 'Capteurs photovoltaïques', 'Photovoltaic Sensors'), ('buildings/reacteur-thermonucleaire', 'Réacteur thermonucléaire', 'Thermonuclear Reactor'), ('ships/collecteur-solaire', 'Collecteur solaire', 'Solar Collector')],
    'economy/storage': [('buildings/depot-alliages', "Dépôt d'alliages", 'Alloy Depot'), ('buildings/chambre-cristalline', 'Chambre cristalline', 'Crystal Chamber'), ('buildings/citerne-hydrogene', "Citerne d'hydrogène", 'Hydrogen Tank')],
    'research/stellar-collaboration': [('research/collaboration-stellaire', 'Collaboration Stellaire', 'Stellar Collaboration')],
    'misc/premium': [('resources/stellar-points', 'Points Stellaires', 'Stellar Points')],
    'players/alliances': [('research/diplomatie-stellaire', 'Diplomatie Stellaire', 'Stellar Diplomacy')],
    'fleet/expeditions': [('research/cosmologie-appliquee', 'Cosmologie Appliquée', 'Astrophysics')],
}
for path, imgs in heads.items():
    for loc, heading, idx in (('fr', '## Règles', 1), ('en', '## Rules', 2)):
        E.setdefault(f'{loc}/{path}', []).extend(header(f'{loc}/{path}', [(i[0], i[idx]) for i in imgs], heading))

# --- Vue galaxie : captures sans coordonnées, positions masquées ---
E['fr/universe/galaxy-view'] = [
    ["![La vue galaxie, en affichage liste](/images/screenshots/french/vue-galaxie.jpg)\n*La vue galaxie, système [2:86], en affichage liste. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*",
     f"![La vue galaxie en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)\n*La vue galaxie en affichage orbites : chaque planète a son aspect, selon son type et son biome. {V_FR}*\n\n![La vue galaxie en affichage liste](/images/screenshots/french/vue-galaxie.jpg)\n*En affichage liste, les positions pas encore espionnées restent illisibles. {V_FR}*"],
    ["4. Pour chaque position occupée, la ligne indique le propriétaire, ses points et ses **statuts**.",
     "4. **Positions masquées** : tant qu'une position n'a pas été espionnée, tout y reste caché. Une écriture exotique, illisible, remplace le nom de la planète et celui de son propriétaire. Une case illisible peut être libre ou occupée : seul l'espionnage le révèle.\n5. Une position **espionnée** dévoile la planète, son propriétaire, ses points et ses **statuts**. Avec Renseignement Tactique 10, une case espionnée reste découverte durablement."],
    ["5. Le compteur", "6. Le compteur"], ["6. Le bouton d'**espionnage rapide**", "7. Le bouton d'**espionnage rapide**"],
    ["7. La fiche d'une case", "8. La fiche d'une case"], ["8. Vous pouvez **partager une position**", "9. Vous pouvez **partager une position**"],
    ["9. Une **étoile**", "10. Une **étoile**"],
    ["- **Le compteur d'attaques est par joueur**", "- **Une case illisible ne dit rien** : elle peut cacher un joueur comme être vide. Envoyez un Éclaireur avant de conclure.\n- **Le compteur d'attaques est par joueur**"],
]
E['en/universe/galaxy-view'] = [
    ["![The galaxy view, list layout](/images/screenshots/english/galaxy-view.jpg)\n*The galaxy view, system [2:86], list layout. Screenshot from game version Server 2.1.0 · Client 3.1.0.*",
     f"![The galaxy view, orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)\n*The galaxy view in orbit layout: each planet has its own look, set by its type and biome. {V_EN}*\n\n![The galaxy view, list layout](/images/screenshots/english/galaxy-view.jpg)\n*In list layout, positions not yet spied on stay unreadable. {V_EN}*"],
    ["4. For each occupied position, the row shows the owner, their points and their **statuses**.",
     "4. **Hidden positions**: until a position has been spied on, everything there stays hidden. An exotic, unreadable script replaces the planet's name and its owner's. An unreadable cell may be free or occupied: only espionage tells.\n5. A **spied** position reveals the planet, its owner, their points and their **statuses**. With Espionage Technology 10, a spied cell stays discovered for good."],
    ["5. The **\"Attacks remaining", "6. The **\"Attacks remaining"], ["6. The **quick spy**", "7. The **quick spy**"],
    ["7. A cell's sheet", "8. A cell's sheet"], ["8. You can **share a position**", "9. You can **share a position**"],
    ["9. A **star**", "10. A **star**"],
    ["- **The attack counter is per player**", "- **An unreadable cell tells nothing**: it may hide a player or be empty. Send a Scout before drawing conclusions.\n- **The attack counter is per player**"],
]

# --- Espionnage : la sonde révèle la carte ---
E['fr/espionage/spying'].append(["ou d'un clic avec le bouton d'espionnage rapide de la [vue galaxie](/fr/universe/galaxy-view).", "ou d'un clic avec le bouton d'espionnage rapide de la [vue galaxie](/fr/universe/galaxy-view). Espionner une case **révèle** aussi, dans la vue galaxie, sa planète et son propriétaire, masqués jusque-là par une écriture illisible."])
E['en/espionage/spying'].append(["or in one click with the quick spy button of the [galaxy view](/en/universe/galaxy-view).", "or in one click with the quick spy button of the [galaxy view](/en/universe/galaxy-view). Spying on a cell also **reveals** its planet and owner in the galaxy view, hidden until then behind an unreadable script."])

# --- Planètes : biome, skins, capture en orbites ---
E['fr/universe/planets'] = [
    ["6. **Type et apparence** : le type (désert, aride, normal, jungle, eau, glace, gaz) et la variante visuelle ne changent que le nom généré et les images. Un skin acheté en boutique remplace l'apparence.",
     "6. **Type, biome et apparence** : chaque planète a un type (désert, aride, normal, jungle, eau, glace, gaz) et un **biome**, une variante visuelle tirée à sa création. Ensemble, ils donnent à chaque planète son aspect propre, dans la vue galaxie comme en 3D. Ils ne changent que le nom généré et les images, pas la production. Un **skin de planète**, obtenu en boutique ou dans le lot mensuel Premium, remplace l'apparence de votre planète."],
    ["\n## Règles\n", f"\n![Un système en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)\n*Un système en affichage orbites : chaque planète a l'aspect de son type et de son biome. {V_FR}*\n\n## Règles\n"],
]
E['en/universe/planets'] = [
    ["6. **Type and look**: the type (desert, dry, normal, jungle, water, ice, gas) and visual variant only change the generated name and the pictures. A skin bought in the shop replaces the look.",
     "6. **Type, biome and look**: each planet has a type (desert, dry, normal, jungle, water, ice, gas) and a **biome**, a visual variant rolled when it is created. Together they give each planet its own look, in the galaxy view as in 3D. They only change the generated name and the pictures, not output. A **planet skin**, from the shop or the Premium monthly set, replaces your planet's look."],
    ["\n## Rules\n", f"\n![A system in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)\n*A system in orbit layout: each planet looks like its type and biome. {V_EN}*\n\n## Rules\n"],
]

# --- Premium : pas de pay to win, skins ---
E['fr/misc/premium'].extend([
    ["## Règles\n\n### Premium\n", "## Règles\n\n### Aucun « pay to win »\nC'est un parti pris fort de Dynasty Nova : dans les univers PvP, **aucun achat ne donne d'avantage de jeu**. On ne peut acheter ni ressources, ni bonus de production, ni accélération de construction, de recherche ou de production militaire. Ce que l'on achète sert à l'apparence (avatars, cadres, couleurs de pseudo, emblèmes, skins de planète), au renommage des planètes et au Premium, qui apporte du confort de jeu.\n\n### Premium\n"],
    ["\n## Exemple chiffré", "\n### Skins de planète\nUn skin remplace l'apparence de votre planète dans le jeu. Il s'obtient en boutique, ou dans le lot mensuel du Premium. Il ne change rien d'autre : ni la production, ni la taille, ni la température.\n\n## Exemple chiffré"],
])
E['en/misc/premium'].extend([
    ["## Rules\n\n### Premium\n", "## Rules\n\n### No pay-to-win\nThis is a strong choice in Dynasty Nova: in PvP universes, **no purchase gives a gameplay advantage**. You cannot buy resources, production bonuses, or speed-ups for construction, research or military production. What you buy is for looks (avatars, frames, username colours, emblems, planet skins), planet renaming and Premium, which adds comfort.\n\n### Premium\n"],
    ["\n## Worked example", "\n### Planet skins\nA skin replaces your planet's look in the game. You get it from the shop, or in the Premium monthly set. It changes nothing else: neither output, size nor temperature.\n\n## Worked example"],
])

# --- Vous venez d'OGame : positions masquées, biomes, pas de pay to win, univers privés ---
E['fr/getting-started/coming-from-ogame'] = [
    ["### Ce qui n'existe pas\n", "### Ce qui n'existe pas\n- **Pay to win** : dans les univers PvP, aucun achat ne donne de ressources, de production ou d'accélération. C'est un parti pris fort, à l'opposé des officiers et de la matière noire.\n"],
    ["### Ce qui est nouveau\n", "### Ce qui est nouveau\n- **Positions masquées** : dans la vue galaxie, une position reste illisible tant qu'elle n'a pas été espionnée. Une écriture exotique cache le nom de la planète et celui de son propriétaire.\n- **Planètes illustrées** : chaque planète a un type et un biome qui fixent son aspect, en liste, en orbites et en 3D. Des **skins de planète** permettent de personnaliser la vôtre.\n- **Univers privés** : vous pouvez ouvrir votre propre univers payant, avec ses joueurs, ses vitesses et ses règles (voir [Univers privés](/fr/misc/private-universes)).\n"],
]
E['en/getting-started/coming-from-ogame'] = [
    ["### What does not exist\n", "### What does not exist\n- **Pay-to-win**: in PvP universes, no purchase gives resources, output or speed-ups. It is a strong choice, the opposite of officers and dark matter.\n"],
    ["### What is new\n", "### What is new\n- **Hidden positions**: in the galaxy view, a position stays unreadable until it has been spied on. An exotic script hides the planet's name and its owner's.\n- **Illustrated planets**: each planet has a type and a biome that set its look, in list, orbit and 3D views. **Planet skins** let you customise yours.\n- **Private universes**: you can open your own paid universe, with its players, speeds and rules (see [Private universes](/en/misc/private-universes)).\n"],
]

out = Path(__file__).with_name('2026-10-02-illustrations.json')
out.write_text(json.dumps(E, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(E), 'pages,', sum(len(v) for v in E.values()), 'remplacements ->', out.name)
