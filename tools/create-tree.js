// Crée l'arborescence du wiki joueurs Dynasty Nova sur Wiki.js 2 (GraphQL).
// À exécuter dans un onglet ouvert sur https://wiki.dynastynova.com, connecté avec un compte
// ayant les droits write:pages. Les pages sont créées non publiées ; celles qui existent déjà sont ignorées.
// Usage : await createTree(['fr', 'en'])  (ajouter 'es' quand la langue sera activée)

const PAGES = [
  // [chemin, rubrique, titre FR, description FR, titre EN, description EN, encart univers]
  ['getting-started', 'getting-started', 'Bien démarrer', 'Tout ce qu\'il faut pour commencer sur Dynasty Nova.', 'Getting started', 'Everything you need to start playing Dynasty Nova.', false],
  ['getting-started/first-steps', 'getting-started', 'Premiers pas', 'Les premières actions à faire sur votre planète.', 'First steps', 'The first things to do on your planet.', false],
  ['getting-started/tutorial-quests', 'getting-started', 'Le didacticiel (quêtes)', 'Les 7 paliers de quêtes, leurs objectifs et leurs récompenses.', 'The tutorial (quests)', 'The 7 quest tiers, their goals and rewards.', false],
  ['getting-started/interface', 'getting-started', 'L\'interface', 'Visite guidée des écrans du jeu.', 'The interface', 'A guided tour of the game screens.', false],
  ['getting-started/glossary', 'getting-started', 'Glossaire et nomenclature', 'Noms des unités en français, anglais et espagnol.', 'Glossary and naming', 'Unit names in French, English and Spanish.', false],
  ['getting-started/coming-from-ogame', 'getting-started', 'Vous venez d\'OGame ?', 'Ce qui change par rapport à OGame.', 'Coming from OGame?', 'What differs from OGame.', false],
  ['getting-started/faq', 'getting-started', 'FAQ', 'Réponses courtes aux questions fréquentes.', 'FAQ', 'Short answers to common questions.', false],

  ['universe', 'universe', 'Univers et planètes', 'Univers, coordonnées, planètes et lunes.', 'Universe and planets', 'Universes, coordinates, planets and moons.', false],
  ['universe/universes', 'universe', 'Les univers', 'Ce qu\'est un univers et ses paramètres.', 'Universes', 'What a universe is and its settings.', true],
  ['universe/coordinates', 'universe', 'Coordonnées', 'Galaxie, système et position.', 'Coordinates', 'Galaxy, system and position.', true],
  ['universe/galaxy-view', 'universe', 'La vue galaxie', 'Lire la vue galaxie, système par système.', 'The galaxy view', 'Reading the galaxy view, system by system.', false],
  ['universe/planets', 'universe', 'Planètes : taille, température, type', 'Cases, température et effet de la position.', 'Planets: size, temperature, type', 'Fields, temperature and the effect of position.', false],
  ['universe/colonization', 'universe', 'Coloniser', 'Fonder des colonies avec le Pionnier spatial.', 'Colonization', 'Founding colonies with the Space Pioneer.', false],
  ['universe/abandoning-a-planet', 'universe', 'Abandonner une colonie', 'Conditions et conséquences d\'un abandon.', 'Abandoning a colony', 'Conditions and consequences of abandoning a colony.', true],
  ['universe/moons', 'universe', 'Les lunes', 'Formation des lunes, Base lunaire et cases.', 'Moons', 'Moon formation, Lunar base and fields.', true],

  ['economy', 'economy', 'Économie', 'Ressources, énergie et bâtiments.', 'Economy', 'Resources, energy and buildings.', false],
  ['economy/resources', 'economy', 'Les ressources', 'Métal, cristal et hydrogène.', 'Resources', 'Metal, crystal and hydrogen.', true],
  ['economy/energy', 'economy', 'L\'énergie', 'Produire et consommer de l\'énergie.', 'Energy', 'Producing and consuming energy.', false],
  ['economy/storage', 'economy', 'Le stockage', 'Capacités de stockage et débordement.', 'Storage', 'Storage capacity and overflow.', false],
  ['economy/buildings', 'economy', 'Liste des bâtiments', 'Tous les bâtiments : rôle, coûts, prérequis.', 'Buildings list', 'All buildings: role, costs, requirements.', true],
  ['economy/formulas', 'economy', 'Formules de l\'économie', 'Coûts, durées, production et points.', 'Economy formulas', 'Costs, durations, production and points.', true],
  ['economy/build-queue', 'economy', 'Files de construction', 'Ordres en file, paiement et annulation.', 'Build queues', 'Queued orders, payment and cancellation.', false],
  ['economy/demolition', 'economy', 'Démolir un bâtiment', 'Rendre un niveau et libérer une case.', 'Demolishing a building', 'Removing a level to free a field.', false],
  ['economy/repair-station', 'economy', 'Station de réparation', 'Récupérer une part des vaisseaux détruits.', 'Repair Station', 'Recovering part of your destroyed ships.', false],
  ['economy/terraformer-and-logistics', 'economy', 'Modulateur planétaire et Centre logistique', 'Agrandir sa planète, débloquer la Diplomatie Stellaire.', 'Planetary Modulator and Logistics Center', 'Enlarging your planet, unlocking Stellar Diplomacy.', false],

  ['research', 'research', 'Recherche', 'Technologies et arbre technologique.', 'Research', 'Technologies and the tech tree.', false],
  ['research/technologies', 'research', 'Liste des technologies', 'Toutes les technologies : effets, coûts, prérequis.', 'Technologies list', 'All technologies: effects, costs, requirements.', true],
  ['research/tech-tree', 'research', 'Arbre technologique', 'Les prérequis de chaque bâtiment, recherche et unité.', 'Tech tree', 'Requirements of every building, research and unit.', false],
  ['research/stellar-collaboration', 'research', 'Collaboration Stellaire', 'Mettre ses Centres d\'innovation en réseau.', 'Stellar Collaboration', 'Networking your Innovation Centers.', false],

  ['fleet', 'fleet', 'Flotte', 'Vaisseaux, déplacements et missions.', 'Fleet', 'Ships, movement and missions.', false],
  ['fleet/ships', 'fleet', 'Liste des vaisseaux', 'Les 14 vaisseaux : coûts, statistiques, prérequis.', 'Ships list', 'The 14 ships: costs, stats, requirements.', false],
  ['fleet/rapid-fire', 'fleet', 'Tirs rapides', 'Quelles unités tirent plusieurs fois sur quelles cibles.', 'Rapid fire', 'Which units fire several times at which targets.', false],
  ['fleet/orbital-dock', 'fleet', 'Dock orbital (chantier)', 'Construire vaisseaux et défenses.', 'Orbital Dock (shipyard)', 'Building ships and defenses.', true],
  ['fleet/movement', 'fleet', 'Déplacements', 'Vitesse, durée de vol et consommation d\'hydrogène.', 'Fleet movement', 'Speed, flight time and hydrogen use.', true],
  ['fleet/missions', 'fleet', 'Les missions', 'Attaque, transport, stationnement, colonisation et les autres.', 'Missions', 'Attack, transport, stationing, colonization and more.', false],
  ['fleet/expeditions', 'fleet', 'Expéditions', 'Explorer l\'inconnu avec sa flotte.', 'Expeditions', 'Exploring the unknown with your fleet.', false],
  ['fleet/jump-gate', 'fleet', 'Porte de saut', 'Déplacer une flotte instantanément entre deux lunes.', 'Jump gate', 'Moving a fleet instantly between two moons.', false],

  ['defense', 'defense', 'Défense', 'Défenses planétaires et missiles.', 'Defense', 'Planetary defenses and missiles.', false],
  ['defense/defenses', 'defense', 'Liste des défenses', 'Les défenses : coûts, statistiques, prérequis.', 'Defenses list', 'Defenses: costs, stats, requirements.', false],
  ['defense/shield-domes', 'defense', 'Barrière défensive et Dôme protecteur', 'Les deux boucliers planétaires.', 'Defensive Barrier and Protective Dome', 'The two planetary shields.', false],
  ['defense/missiles', 'defense', 'Missiles', 'Arsenal balistique, Intercepteurs et Ogives longue portée.', 'Missiles', 'Ballistic Arsenal, Interceptors and Long-Range Warheads.', true],

  ['combat', 'combat', 'Combat', 'Déroulement des combats et leurs suites.', 'Combat', 'How battles work and what follows.', false],
  ['combat/how-combat-works', 'combat', 'Déroulement d\'un combat', 'Tours, tirs, boucliers et tirs rapides.', 'How combat works', 'Rounds, shots, shields and rapid fire.', false],
  ['combat/battle-report', 'combat', 'Lire un rapport de combat', 'Comprendre chaque partie du rapport.', 'Reading a battle report', 'Understanding each part of the report.', false],
  ['combat/plunder', 'combat', 'Pillage', 'Ce que l\'attaquant emporte.', 'Plunder', 'What the attacker takes home.', true],
  ['combat/debris', 'combat', 'Champs de débris', 'Débris créés par les combats et recyclage.', 'Debris fields', 'Debris created by battles and recycling.', true],
  ['combat/defense-rebuild', 'combat', 'Reconstruction des défenses', 'Les défenses détruites reviennent en partie.', 'Defense rebuild', 'Destroyed defenses partly come back.', false],
  ['combat/simulator', 'combat', 'Simulateur de combat', 'Préparer une attaque avec le simulateur.', 'Battle simulator', 'Planning an attack with the simulator.', false],
  ['combat/moon-destruction', 'combat', 'Destruction de lune', 'Détruire une lune avec des Colossus stellaires.', 'Moon destruction', 'Destroying a moon with Stellar Colossi.', false],

  ['espionage', 'espionage', 'Espionnage', 'Sondes, rapports et phalange.', 'Espionage', 'Probes, reports and the phalanx.', false],
  ['espionage/spying', 'espionage', 'Espionner', 'Envoyer des Éclaireurs et ce qu\'ils rapportent.', 'Spying', 'Sending Scouts and what they bring back.', false],
  ['espionage/spy-report', 'espionage', 'Lire un rapport d\'espionnage', 'Les sections du rapport et ce qui les débloque.', 'Reading a spy report', 'Report sections and what unlocks them.', false],
  ['espionage/sensor-phalanx', 'espionage', 'Phalange de capteur', 'Observer les flottes depuis une lune.', 'Sensor phalanx', 'Watching fleets from a moon.', false],

  ['players', 'players', 'Joueurs et règles', 'Classements, protections, alliances et règlement.', 'Players and rules', 'Rankings, protections, alliances and rules.', false],
  ['players/rankings', 'players', 'Classements et points', 'Les quatre classements et le calcul des points.', 'Rankings and points', 'The four rankings and how points are counted.', false],
  ['players/beginner-protection', 'players', 'Protection des débutants', 'Qui peut attaquer qui selon les points.', 'Beginner protection', 'Who can attack whom, based on points.', true],
  ['players/attack-limit', 'players', 'Limite d\'attaques', '6 attaques par joueur sur 24 heures glissantes.', 'Attack limit', '6 attacks per player over a rolling 24 hours.', true],
  ['players/vacation-mode', 'players', 'Mode vacances', 'Mettre son empire en pause.', 'Vacation mode', 'Pausing your empire.', false],
  ['players/inactivity', 'players', 'Inactivité', 'Ce qui arrive à un joueur inactif.', 'Inactivity', 'What happens to an inactive player.', true],
  ['players/alliances', 'players', 'Alliances', 'Créer, rejoindre et gérer une alliance.', 'Alliances', 'Founding, joining and running an alliance.', false],
  ['players/pacts-and-wars', 'players', 'Pactes, fair-play et guerres', 'Les relations entre alliances.', 'Pacts, fair play and wars', 'Relations between alliances.', false],
  ['players/alliance-missions', 'players', 'Missions et station d\'alliance', 'Missions communes, station, talents et trésorerie.', 'Alliance missions and station', 'Shared missions, station, talents and treasury.', false],
  ['players/messages-and-reports', 'players', 'Messagerie et rapports', 'Messages, rapports et partage.', 'Messages and reports', 'Messages, reports and sharing.', false],
  ['players/game-rules', 'players', 'Règlement', 'Les règles du jeu à respecter.', 'Game rules', 'The rules every player must follow.', false],

  ['misc', 'misc', 'Divers', 'Maintenance, Premium et autres sujets.', 'Miscellaneous', 'Maintenance, Premium and other topics.', false],
  ['misc/maintenance', 'misc', 'Maintenance', 'Ce qui est suspendu pendant une maintenance.', 'Maintenance', 'What is suspended during maintenance.', false],
  ['misc/premium', 'misc', 'Premium, boutique et Points stellaires', 'Ce que le Premium et la boutique apportent.', 'Premium, shop and Stellar Points', 'What Premium and the shop provide.', false],
  ['misc/empire-and-bookmarks', 'misc', 'Vue Empire et favoris', 'Suivre toutes ses planètes et ses positions favorites.', 'Empire view and bookmarks', 'Tracking all your planets and favourite positions.', false],
  ['misc/referral', 'misc', 'Parrainage', 'Inviter des joueurs et être récompensé.', 'Referral', 'Inviting players and earning rewards.', false],
  ['misc/changelog', 'misc', 'Historique du wiki', 'Les modifications du wiki, date par date.', 'Wiki changelog', 'Wiki changes, date by date.', false],
];

const LABELS = {
  fr: {
    wip: 'Page en cours de rédaction.',
    universe: '> **Paramètre d\'univers** : certaines valeurs de cette page peuvent être différentes selon l\'univers.\n{.is-info}',
    short: 'En bref', rules: 'Règles', example: 'Exemple chiffré', data: 'Données détaillées',
    pitfalls: 'Pièges fréquents', ogame: 'Différences avec OGame', related: 'Pages liées',
    index: 'Pages de cette rubrique',
  },
  en: {
    wip: 'This page is being written.',
    universe: '> **Universe setting**: some values on this page may differ from one universe to another.\n{.is-info}',
    short: 'In short', rules: 'Rules', example: 'Worked example', data: 'Detailed data',
    pitfalls: 'Common pitfalls', ogame: 'Differences from OGame', related: 'Related pages',
    index: 'Pages in this section',
  },
  es: {
    wip: 'Página en redacción.',
    universe: '> **Parámetro de universo**: algunos valores de esta página pueden variar según el universo.\n{.is-info}',
    short: 'En resumen', rules: 'Reglas', example: 'Ejemplo numérico', data: 'Datos detallados',
    pitfalls: 'Errores frecuentes', ogame: 'Diferencias con OGame', related: 'Páginas relacionadas',
    index: 'Páginas de esta sección',
  },
};

function pageText(page, locale) {
  const [path, , titleFr, descFr, titleEn, descEn, universeBox] = page;
  const L = LABELS[locale];
  const title = locale === 'fr' ? titleFr : titleEn;
  const desc = locale === 'fr' ? descFr : descEn;
  const isIndex = !path.includes('/');
  const parts = [`# ${title}`, '', `> ${L.wip}`, '{.is-warning}', '', `**${desc}**`, ''];
  if (isIndex) {
    parts.push(`## ${L.index}`, '');
    for (const p of PAGES.filter(x => x[0].startsWith(path + '/'))) {
      parts.push(`- [${locale === 'fr' ? p[2] : p[4]}](/${locale}/${p[0]})`);
    }
  } else {
    if (universeBox) parts.push(L.universe, '');
    for (const h of (path === 'getting-started/coming-from-ogame' ? [L.short, L.rules, L.example, L.data, L.pitfalls, L.ogame, L.related] : [L.short, L.rules, L.example, L.data, L.pitfalls, L.related])) parts.push(`## ${h}`, '');
  }
  return { title, description: desc, content: parts.join('\n') + '\n' };
}

async function gql(query, variables) {
  const r = await fetch('/graphql', {
    method: 'POST', credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, variables }),
  });
  return r.json();
}

const CREATE = `mutation($content:String!,$description:String!,$editor:String!,$isPublished:Boolean!,$isPrivate:Boolean!,$locale:String!,$path:String!,$tags:[String]!,$title:String!){pages{create(content:$content,description:$description,editor:$editor,isPublished:$isPublished,isPrivate:$isPrivate,locale:$locale,path:$path,tags:$tags,title:$title){responseResult{succeeded errorCode message}}}}`;

async function createTree(locales = ['fr', 'en']) {
  const existing = await gql('{ pages { list(limit:1000) { path locale } } }');
  const have = new Set((existing.data?.pages?.list || []).map(p => p.locale + '/' + p.path));
  const report = { created: [], skipped: [], failed: [] };
  for (const locale of locales) {
    for (const page of PAGES) {
      const key = locale + '/' + page[0];
      if (have.has(key)) { report.skipped.push(key); continue; }
      // Les pages ES reprennent les textes EN tant que la traduction n'est pas faite.
      const { title, description, content } = pageText(page, locale === 'es' ? 'en' : locale);
      const res = await gql(CREATE, {
        content: locale === 'es' ? content.replace(LABELS.en.wip, LABELS.es.wip) : content,
        description, editor: 'markdown', isPublished: false, isPrivate: false,
        locale, path: page[0], tags: [page[1]], title,
      });
      const rr = res.data?.pages?.create?.responseResult;
      if (rr?.succeeded) report.created.push(key);
      else report.failed.push(key + ' ' + (rr ? rr.errorCode : JSON.stringify(res.errors || res).slice(0, 120)));
    }
  }
  return report;
}
