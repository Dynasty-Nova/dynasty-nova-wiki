"""Synchronise les pages markdown locales avec Wiki.js (API GraphQL).

Le markdown local est la source de vérité : on modifie d'abord le fichier, puis on le pousse.

Authentification : une clé d'API Wiki.js propre à l'agent ou à la personne qui lance l'outil
(Administration > Accès API), jamais le compte ni la session d'un autre utilisateur.
  export WIKIJS_API_KEY=...                          # obligatoire, ne jamais la committer
  export WIKIJS_URL=https://wiki.dynastynova.com     # facultatif (valeur par défaut)

Commandes (chemins relatifs au dossier wiki/, ex. pages/fr/fleet/movement.md) :
  status [fichiers...]      compare le corps local et le corps en ligne (toutes les pages par défaut)
  push FICHIERS...          pousse des pages existantes, vérifie l'empreinte, met à jour `updated`
  create FICHIERS...        crée des pages sans `wiki_id`, puis écrit `wiki_id`, `created`, `updated`
  pull FICHIERS...          remplace le corps local par la version en ligne (récupérer une modification faite sur le wiki)
  upload DOSSIER_ID FICHIERS...   téléverse des images dans un dossier d'assets (même nom = remplacement)

`push` refuse une page modifiée en ligne depuis la dernière synchronisation (date en ligne différente
du `updated` local et corps différent) : faire `pull`, fusionner, puis pousser. `--force` passe outre.
"""
import hashlib
import json
import mimetypes
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEPARATOR = '\n---\n\n'
URL = os.environ.get('WIKIJS_URL', 'https://wiki.dynastynova.com').rstrip('/')
# Cloudflare refuse l'agent par défaut de Python (« Python-urllib ») avec un 403.
USER_AGENT = 'dynasty-nova-wiki-tools/1.0'
FIELDS = 'id locale path title description isPublished isPrivate editor scriptCss scriptJs updatedAt createdAt content tags { tag }'


# Front matter : une ligne `clé: valeur` par champ, valeurs au format JSON.

def read_page(path):
    text = Path(path).read_text(encoding='utf-8')
    head, body = text.split(SEPARATOR, 1)
    meta = {}
    for line in head.splitlines()[1:]:
        key, _, value = line.partition(': ')
        meta[key] = json.loads(value)
    return meta, body


def write_page(path, meta, body):
    lines = ['---'] + [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in meta.items()]
    Path(path).write_text('\n'.join(lines) + SEPARATOR + body, encoding='utf-8')


def digest(body):
    return hashlib.sha256(body.encode('utf-8')).hexdigest()


def local_files(args):
    if args:
        return [ROOT / a if not Path(a).is_absolute() else Path(a) for a in args]
    return sorted((ROOT / 'pages').rglob('*.md'))


# API

def token():
    key = os.environ.get('WIKIJS_API_KEY')
    if not key:
        sys.exit('WIKIJS_API_KEY manquante : créer une clé d\'API dédiée dans Wiki.js (Administration > Accès API).')
    return key


def gql(query, variables=None):
    data = json.dumps({'query': query, 'variables': variables or {}}).encode()
    req = urllib.request.Request(f'{URL}/graphql', data=data, headers={
        'Content-Type': 'application/json', 'Authorization': f'Bearer {token()}', 'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as res:
        out = json.load(res)
    if out.get('errors'):
        raise RuntimeError(out['errors'])
    return out['data']


def fetch(ids):
    """Récupère plusieurs pages par lots, via des alias GraphQL."""
    pages = {}
    ids = list(ids)
    for i in range(0, len(ids), 20):
        chunk = ids[i:i + 20]
        query = '{ pages { ' + ' '.join(f'p{n}: single(id: {n}) {{ {FIELDS} }}' for n in chunk) + ' } }'
        for value in gql(query)['pages'].values():
            pages[value['id']] = value
    return pages


def check(result, label):
    rr = result['responseResult']
    if not rr['succeeded']:
        raise RuntimeError(f'{label} : {rr.get("errorCode")} {rr.get("message")}')


# Commandes

def cmd_status(args):
    files = local_files(args)
    pages = {f: read_page(f) for f in files}
    remote = fetch(m['wiki_id'] for m, _ in pages.values() if m.get('wiki_id'))
    differ = 0
    for f, (meta, body) in pages.items():
        rel = f.relative_to(ROOT)
        page = remote.get(meta.get('wiki_id'))
        if page is None:
            print(f'ABSENT    {rel}')
            differ += 1
        elif digest(page['content']) != digest(body):
            edited = page['updatedAt'] != meta.get('updated')
            print(f'{"EN LIGNE" if edited else "LOCAL   "}  {rel}  (en ligne {page["updatedAt"]}, local {meta.get("updated")})')
            differ += 1
    print(f'{len(pages) - differ}/{len(pages)} identiques')
    print('EN LIGNE = modifiée sur le wiki depuis la dernière synchro (faire pull) ; LOCAL = à pousser')


def update_variables(page, meta, body):
    return {
        'id': page['id'], 'content': body, 'title': meta['title'], 'description': meta['description'],
        'isPublished': meta['published'], 'isPrivate': page['isPrivate'], 'locale': meta['locale'],
        'path': meta['path'], 'editor': page['editor'], 'tags': meta['tags'],
        'scriptCss': page['scriptCss'] or '', 'scriptJs': page['scriptJs'] or '',
        'publishStartDate': '', 'publishEndDate': ''}


UPDATE = '''mutation($id: Int!, $content: String!, $title: String!, $description: String!, $isPublished: Boolean!,
  $isPrivate: Boolean!, $locale: String!, $path: String!, $editor: String!, $tags: [String]!, $scriptCss: String,
  $scriptJs: String, $publishStartDate: Date, $publishEndDate: Date) {
  pages { update(id: $id, content: $content, title: $title, description: $description, isPublished: $isPublished,
    isPrivate: $isPrivate, locale: $locale, path: $path, editor: $editor, tags: $tags, scriptCss: $scriptCss,
    scriptJs: $scriptJs, publishStartDate: $publishStartDate, publishEndDate: $publishEndDate) {
    responseResult { succeeded errorCode message } } } }'''

CREATE = '''mutation($content: String!, $title: String!, $description: String!, $isPublished: Boolean!,
  $locale: String!, $path: String!, $tags: [String]!) {
  pages { create(content: $content, title: $title, description: $description, isPublished: $isPublished,
    isPrivate: false, locale: $locale, path: $path, editor: "markdown", tags: $tags, scriptCss: "", scriptJs: "",
    publishStartDate: "", publishEndDate: "") {
    responseResult { succeeded errorCode message } page { id } } } }'''


def verify_and_stamp(f, meta, body):
    page = fetch([meta['wiki_id']])[meta['wiki_id']]
    if digest(page['content']) != digest(body):
        raise RuntimeError(f'{f.relative_to(ROOT)} : empreinte différente après envoi')
    meta['updated'] = page['updatedAt']
    meta.setdefault('created', page['createdAt'])
    write_page(f, meta, body)
    print(f'ok {f.relative_to(ROOT)} {digest(body)[:16]}')


def cmd_push(args):
    force = '--force' in args
    files = local_files([a for a in args if a != '--force'])
    for f in files:
        meta, body = read_page(f)
        page = fetch([meta['wiki_id']])[meta['wiki_id']]
        if digest(page['content']) == digest(body) and page['title'] == meta['title']:
            print(f'inchangé {f.relative_to(ROOT)}')
            continue
        if not force and page['updatedAt'] != meta.get('updated') and digest(page['content']) != digest(body):
            print(f'REFUS {f.relative_to(ROOT)} : modifiée en ligne le {page["updatedAt"]} (pull puis fusion, ou --force)')
            continue
        check(gql(UPDATE, update_variables(page, meta, body))['pages']['update'], f)
        verify_and_stamp(f, meta, body)


def cmd_create(args):
    for f in local_files(args):
        meta, body = read_page(f)
        if meta.get('wiki_id'):
            print(f'déjà créée {f.relative_to(ROOT)} (wiki_id {meta["wiki_id"]})')
            continue
        result = gql(CREATE, {'content': body, 'title': meta['title'], 'description': meta['description'],
                              'isPublished': meta['published'], 'locale': meta['locale'], 'path': meta['path'],
                              'tags': meta['tags']})['pages']['create']
        check(result, f)
        meta = {'wiki_id': result['page']['id'], **meta}
        meta['url'] = f'{URL}/{meta["locale"]}/{meta["path"]}'
        verify_and_stamp(f, meta, body)


def cmd_pull(args):
    for f in local_files(args):
        meta, _ = read_page(f)
        page = fetch([meta['wiki_id']])[meta['wiki_id']]
        meta['updated'] = page['updatedAt']
        write_page(f, meta, page['content'])
        print(f'récupérée {f.relative_to(ROOT)} (en ligne {page["updatedAt"]})')


def cmd_upload(args):
    folder_id, files = int(args[0]), args[1:]
    for name in files:
        path = Path(name)
        boundary = uuid.uuid4().hex
        mime = mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
        parts = [
            f'--{boundary}\r\nContent-Disposition: form-data; name="mediaUpload"\r\n\r\n'.encode()
            + json.dumps({'folderId': folder_id}).encode() + b'\r\n',
            f'--{boundary}\r\nContent-Disposition: form-data; name="mediaUpload"; filename="{path.name}"\r\n'
            f'Content-Type: {mime}\r\n\r\n'.encode() + path.read_bytes() + b'\r\n',
            f'--{boundary}--\r\n'.encode()]
        req = urllib.request.Request(f'{URL}/u', data=b''.join(parts), headers={
            'Content-Type': f'multipart/form-data; boundary={boundary}', 'Authorization': f'Bearer {token()}', 'User-Agent': USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=120) as res:
                print(f'ok {path.name} ({res.status})')
        except urllib.error.HTTPError as e:
            print(f'ÉCHEC {path.name} : {e.code} {e.read()[:200]!r}')


COMMANDS = {'status': cmd_status, 'push': cmd_push, 'create': cmd_create, 'pull': cmd_pull, 'upload': cmd_upload}

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    COMMANDS[sys.argv[1]](sys.argv[2:])
